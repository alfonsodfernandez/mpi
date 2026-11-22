import React, { useEffect, useRef, useState } from "react";
import { ExercisePrompt, ProtectedCanvasSpec } from "../types";
import { CodeBlock, MathText } from "./MathText";

interface ProtectedPromptProps {
  prompt: ExercisePrompt;
  studentName: string;
  watermarkBase: string;
  onBlockedAction?: (violationType: string, details: string) => void;
}

/**
 * Renderiza matrices o sistemas críticos directamente sobre un <canvas> con marcas de agua
 * y perturbación anti-OCR sutil (nítido al ojo humano, difícil de copiar/extraer automáticamente).
 */
const AntiOcrMatrixCanvas: React.FC<{
  spec: ProtectedCanvasSpec;
  watermarkLabel: string;
  tick: number;
}> = ({ spec, watermarkLabel, tick }) => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    let width = 420;
    let height = 148;

    if (spec.kind === "text_lines" && spec.lines) {
      width = 460;
      height = Math.max(115, 42 + spec.lines.length * 30);
    } else if (spec.kind === "matrix" && spec.rows) {
      const cols = spec.rows[0]?.length || 3;
      width = Math.max(290, 90 + cols * 74);
      height = Math.max(124, 48 + spec.rows.length * 34);
    } else if (spec.kind === "augmented_matrix" && spec.left) {
      const cols = (spec.left[0]?.length || 3) + 1;
      width = Math.max(360, 110 + cols * 78);
      height = Math.max(124, 48 + spec.left.length * 34);
    }

    canvas.width = width * dpr;
    canvas.height = height * dpr;
    canvas.style.width = `${width}px`;
    canvas.style.height = `${height}px`;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    // Fondo oscuro con textura micro-ruido anti-OCR
    ctx.fillStyle = "#0a0e16";
    ctx.fillRect(0, 0, width, height);

    // Líneas finas diagonales sutiles
    ctx.strokeStyle = "rgba(56, 189, 248, 0.065)";
    ctx.lineWidth = 1;
    const shift = (tick * 7) % 28;
    for (let x = -height; x < width + height; x += 26) {
      ctx.beginPath();
      ctx.moveTo(x + shift, 0);
      ctx.lineTo(x - height + shift, height);
      ctx.stroke();
    }

    // Marca de agua dinámica en el fondo del canvas
    ctx.save();
    ctx.translate(width / 2, height / 2);
    ctx.rotate(-0.22);
    ctx.font = '600 11px "JetBrains Mono", monospace';
    ctx.fillStyle = "rgba(245, 158, 11, 0.14)";
    ctx.textAlign = "center";
    ctx.fillText(watermarkLabel, 0, -18);
    ctx.fillText(watermarkLabel, 0, 24);
    ctx.restore();

    // Etiqueta superior
    ctx.font = '600 11px "JetBrains Mono", monospace';
    ctx.fillStyle = "#64748b";
    ctx.textAlign = "left";
    ctx.fillText(`VISTA PROTEGIDA · ${spec.label.toUpperCase()}`, 14, 20);

    // Dibujo de contenido matemático
    ctx.fillStyle = "#f1f5f9";
    ctx.font = '600 16px "JetBrains Mono", monospace';

    if (spec.kind === "text_lines" && spec.lines) {
      ctx.textAlign = "left";
      spec.lines.forEach((line, idx) => {
        const jitterY = ((idx + tick) % 2 === 0 ? 0.4 : -0.4);
        ctx.fillText(line, 24, 54 + idx * 30 + jitterY);
      });
    } else if (spec.kind === "matrix" && spec.rows) {
      const rows = spec.rows;
      const nR = rows.length;
      const nC = rows[0]?.length || 1;
      const topY = 38;
      const botY = topY + nR * 32;
      const leftX = 36;
      const rightX = width - 36;

      // Corchetes de matriz
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(leftX + 10, topY);
      ctx.lineTo(leftX, topY);
      ctx.lineTo(leftX, botY);
      ctx.lineTo(leftX + 10, botY);
      ctx.moveTo(rightX - 10, topY);
      ctx.lineTo(rightX, topY);
      ctx.lineTo(rightX, botY);
      ctx.lineTo(rightX - 10, botY);
      ctx.stroke();

      const colW = (rightX - leftX - 24) / nC;
      ctx.textAlign = "center";
      ctx.fillStyle = "#f1f5f9";
      rows.forEach((row, r) => {
        row.forEach((cell, c) => {
          const cx = leftX + 12 + colW * (c + 0.5);
          const cy = topY + 22 + r * 32 + ((r + c) % 2 === 0 ? 0.5 : -0.5);
          ctx.fillText(cell, cx, cy);
        });
      });
    } else if (spec.kind === "augmented_matrix" && spec.left && spec.right) {
      const left = spec.left;
      const right = spec.right;
      const nR = left.length;
      const nC = left[0]?.length || 1;
      const topY = 38;
      const botY = topY + nR * 32;
      const leftX = 32;
      const rightX = width - 32;

      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(leftX + 10, topY);
      ctx.lineTo(leftX, topY);
      ctx.lineTo(leftX, botY);
      ctx.lineTo(leftX + 10, botY);
      ctx.moveTo(rightX - 10, topY);
      ctx.lineTo(rightX, topY);
      ctx.lineTo(rightX, botY);
      ctx.lineTo(rightX - 10, botY);
      ctx.stroke();

      const innerW = rightX - leftX - 24;
      const colW = innerW / (nC + 1);
      const sepX = leftX + 12 + colW * nC;

      // Barra vertical de matriz ampliada
      ctx.strokeStyle = "rgba(245, 158, 11, 0.7)";
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 3]);
      ctx.beginPath();
      ctx.moveTo(sepX, topY + 4);
      ctx.lineTo(sepX, botY - 4);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.textAlign = "center";
      ctx.fillStyle = "#f1f5f9";
      left.forEach((row, r) => {
        row.forEach((cell, c) => {
          const cx = leftX + 12 + colW * (c + 0.5);
          const cy = topY + 22 + r * 32;
          ctx.fillText(cell, cx, cy);
        });
        ctx.fillStyle = "#fcd34d";
        ctx.fillText(right[r] || "0", sepX + colW * 0.5, topY + 22 + r * 32);
        ctx.fillStyle = "#f1f5f9";
      });
    }

    // Borde del canvas
    ctx.strokeStyle = "#232c3f";
    ctx.lineWidth = 1;
    ctx.strokeRect(0.5, 0.5, width - 1, height - 1);
  }, [spec, watermarkLabel, tick]);

  return (
    <div className="protected-matrix-canvas-wrap">
      <canvas
        ref={canvasRef}
        onContextMenu={(e) => e.preventDefault()}
        style={{ borderRadius: 8, maxWidth: "100%", height: "auto" }}
      />
    </div>
  );
};

export const ProtectedPrompt: React.FC<ProtectedPromptProps> = ({
  prompt,
  studentName,
  watermarkBase,
  onBlockedAction,
}) => {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const wmCanvasRef = useRef<HTMLCanvasElement | null>(null);
  const [tick, setTick] = useState(0);
  const [clockText, setClockText] = useState(() => new Date().toLocaleTimeString("es-ES"));

  useEffect(() => {
    const id = window.setInterval(() => {
      setTick((t) => t + 1);
      setClockText(new Date().toLocaleTimeString("es-ES"));
    }, 1000);
    return () => window.clearInterval(id);
  }, []);

  const liveWatermark = `${studentName.toUpperCase()} · ${clockText} · ${watermarkBase.slice(-11)}`;

  useEffect(() => {
    const container = containerRef.current;
    const canvas = wmCanvasRef.current;
    if (!container || !canvas) return;
    const rect = container.getBoundingClientRect();
    const w = Math.max(300, Math.floor(rect.width));
    const h = Math.max(180, Math.floor(rect.height));

    canvas.width = w;
    canvas.height = h;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    ctx.clearRect(0, 0, w, h);

    // Micro-patrón anti-OCR de baja opacidad
    ctx.save();
    ctx.font = '600 11px "JetBrains Mono", monospace';
    ctx.fillStyle = "rgba(148, 163, 184, 0.09)";
    ctx.rotate(-0.28);

    const stepX = 285;
    const stepY = 78;
    const drift = (tick * 3) % 40;
    for (let y = -h; y < h * 1.8; y += stepY) {
      for (let x = -w; x < w * 1.8; x += stepX) {
        ctx.fillText(liveWatermark, x + drift, y);
      }
    }
    ctx.restore();
  }, [liveWatermark, tick, prompt]);

  const blockEvent = (type: string, details: string) => (e: React.SyntheticEvent) => {
    e.preventDefault();
    e.stopPropagation();
    onBlockedAction?.(type, details);
  };

  return (
    <div
      ref={containerRef}
      className="protected-zone"
      onCopy={blockEvent("COPY_ATTEMPT", "Intento de copiar enunciado protegido")}
      onCut={blockEvent("COPY_ATTEMPT", "Intento de cortar enunciado protegido")}
      onContextMenu={blockEvent("CONTEXT_MENU", "Clic derecho bloqueado sobre enunciado")}
      onDragStart={(e) => e.preventDefault()}
    >
      <canvas ref={wmCanvasRef} className="watermark-overlay" aria-hidden="true" />
      <div className="protected-content">
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            marginBottom: 12,
            fontSize: 11,
            fontFamily: "var(--font-mono)",
            color: "var(--text-muted)",
          }}
        >
          <span>ENUNCIADO BLINDADO · ANTI-COPIA / ANTI-OCR ACTIVO</span>
          <span style={{ color: "var(--accent-amber)" }}>{liveWatermark}</span>
        </div>

        <MathText content={prompt.statement_md} />

        {prompt.code_block && (
          <CodeBlock code={prompt.code_block} language="matlab" protectedMode />
        )}

        {prompt.protected_canvas && (
          <AntiOcrMatrixCanvas
            spec={prompt.protected_canvas}
            watermarkLabel={liveWatermark}
            tick={tick}
          />
        )}
      </div>
    </div>
  );
};
