import React, { useMemo } from "react";
import katex from "katex";
import hljs from "highlight.js/lib/core";
import matlab from "highlight.js/lib/languages/matlab";
import plaintext from "highlight.js/lib/languages/plaintext";

hljs.registerLanguage("matlab", matlab);
hljs.registerLanguage("text", plaintext);

function escapeHtml(text: string): string {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function renderLatex(expr: string, displayMode: boolean): string {
  try {
    return katex.renderToString(expr.trim(), {
      displayMode,
      throwOnError: false,
      strict: false,
      trust: false,
    });
  } catch {
    return `<code>${escapeHtml(expr)}</code>`;
  }
}

export const CodeBlock: React.FC<{
  code: string;
  language?: string;
  label?: string;
  protectedMode?: boolean;
}> = ({ code, language = "matlab", label, protectedMode = false }) => {
  const highlighted = useMemo(() => {
    try {
      const lang = hljs.getLanguage(language) ? language : "plaintext";
      return hljs.highlight(code, { language: lang }).value;
    } catch {
      return escapeHtml(code);
    }
  }, [code, language]);

  return (
    <div className="code-block-wrap">
      <div className="code-block-header">
        <span>{label || (language === "matlab" ? "MATLAB Live Script" : language.toUpperCase())}</span>
        {protectedMode && <span style={{ color: "#f59e0b" }}>SOLO LECTURA · PROTEGIDO</span>}
      </div>
      <pre>
        <code dangerouslySetInnerHTML={{ __html: highlighted }} />
      </pre>
    </div>
  );
};

function renderRichMathMarkdown(source: string): string {
  if (!source) return "";

  const placeholders: string[] = [];
  const hold = (html: string): string => {
    const idx = placeholders.length;
    placeholders.push(html);
    return `@@HOLD_${idx}@@`;
  };

  let text = source.replace(/\r\n/g, "\n");

  // 1. Extraer bloques de código ```lang ... ```
  text = text.replace(/```([a-zA-Z0-9_-]*)\n([\s\S]*?)```/g, (_m, lang: string, body: string) => {
    const useLang = lang && hljs.getLanguage(lang.toLowerCase()) ? lang.toLowerCase() : "plaintext";
    const hl = hljs.highlight(body.trimEnd(), { language: useLang }).value;
    return hold(
      `<div class="code-block-wrap"><div class="code-block-header"><span>${escapeHtml(
        (lang || "TEXT").toUpperCase()
      )}</span></div><pre><code>${hl}</code></pre></div>`
    );
  });

  // 2. Extraer bloques matemáticos display $$ ... $$
  text = text.replace(/\$\$([\s\S]*?)\$\$/g, (_m, expr: string) => hold(renderLatex(expr, true)));

  // 3. Extraer código en línea `...`
  text = text.replace(/`([^`\n]+)`/g, (_m, code: string) => hold(`<code>${escapeHtml(code)}</code>`));

  // 4. Extraer matemáticas inline $...$
  text = text.replace(/\$([^$\n]+?)\$/g, (_m, expr: string) => hold(renderLatex(expr, false)));

  // 5. Escapar HTML restante
  text = escapeHtml(text);

  // 6. Negrita y cursiva
  text = text.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  text = text.replace(/\*([^*\n]+)\*/g, "<em>$1</em>");

  // 7. Párrafos y listas simples
  const lines = text.split("\n");
  const out: string[] = [];
  let inList = false;

  const closeList = () => {
    if (inList) {
      out.push("</ul>");
      inList = false;
    }
  };

  for (const rawLine of lines) {
    const line = rawLine.trim();
    if (!line) {
      closeList();
      continue;
    }
    if (line.startsWith("##### ")) {
      closeList();
      out.push(`<h5 style="margin:12px 0 6px;color:#38bdf8;font-size:13.5px">${line.slice(6)}</h5>`);
    } else if (line.startsWith("#### ")) {
      closeList();
      out.push(`<h4 style="margin:14px 0 6px;color:#f1f5f9;font-size:15px">${line.slice(5)}</h4>`);
    } else if (line.startsWith("### ")) {
      closeList();
      out.push(`<h3 style="margin:16px 0 8px;color:#f1f5f9;font-size:16.5px">${line.slice(4)}</h3>`);
    } else if (/^[-•]\s+/.test(line)) {
      if (!inList) {
        out.push('<ul style="margin:6px 0 10px 18px;padding:0;display:flex;flex-direction:column;gap:4px">');
        inList = true;
      }
      out.push(`<li>${line.replace(/^[-•]\s+/, "")}</li>`);
    } else if (/^@@HOLD_\d+@@$/.test(line)) {
      closeList();
      out.push(line);
    } else {
      closeList();
      out.push(`<p>${line}</p>`);
    }
  }
  closeList();

  let finalHtml = out.join("\n");
  finalHtml = finalHtml.replace(/@@HOLD_(\d+)@@/g, (_m, idxStr: string) => placeholders[Number(idxStr)] || "");
  return finalHtml;
}

export const MathText: React.FC<{ content: string; className?: string }> = ({ content, className = "" }) => {
  const html = useMemo(() => renderRichMathMarkdown(content), [content]);
  return <div className={`math-prose ${className}`} dangerouslySetInnerHTML={{ __html: html }} />;
};
