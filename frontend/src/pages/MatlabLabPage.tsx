import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { BookMarked, CheckCircle2, Cpu, Terminal } from "lucide-react";
import { apiFetch } from "../api/client";
import { CodeBlock, MathText } from "../components/MathText";

export const MatlabLabPage: React.FC = () => {
  const navigate = useNavigate();
  const [data, setData] = useState<any>(null);
  const [tab, setTab] = useState<"chuleta" | "cuaderno" | "rubrica" | "practicas">("chuleta");
  const [selectedGuide, setSelectedGuide] = useState<string>("matlab_01");

  useEffect(() => {
    apiFetch<any>("/api/content/matlab").then((res) => {
      setData(res);
      if (res?.guides?.[0]) setSelectedGuide(res.guides[0].id);
    });
  }, []);

  if (!data) return <div className="panel">Cargando Laboratorio MATLAB...</div>;

  const activeGuide = data.guides.find((g: any) => g.id === selectedGuide) || data.guides[0];

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
      <div className="page-header">
        <div>
          <h1 className="page-title">Laboratorio MATLAB · Álgebra Aplicada</h1>
          <p className="page-subtitle">
            Chuleta oficial de funciones, rúbrica <code>Formato_practicas_Matlab_2026</code>, 8 guiones del cuaderno común y prácticas evaluables 1–3.
          </p>
        </div>
        <button
          type="button"
          className="btn btn-primary"
          onClick={() => navigate("/ejercicios?topic=matlab")}
        >
          <Cpu size={16} /> Retos de Interpretación de Código (Lockdown)
        </button>
      </div>

      <div className="tabs">
        <button type="button" className={`tab-btn ${tab === "chuleta" ? "active" : ""}`} onClick={() => setTab("chuleta")}>
          Chuleta de Funciones
        </button>
        <button type="button" className={`tab-btn ${tab === "cuaderno" ? "active" : ""}`} onClick={() => setTab("cuaderno")}>
          Cuaderno Común (8 Aplicaciones)
        </button>
        <button type="button" className={`tab-btn ${tab === "rubrica" ? "active" : ""}`} onClick={() => setTab("rubrica")}>
          Rúbrica Oficial UFV 2026
        </button>
        <button type="button" className={`tab-btn ${tab === "practicas" ? "active" : ""}`} onClick={() => setTab("practicas")}>
          Prácticas Evaluables 1–3
        </button>
      </div>

      {tab === "chuleta" && (
        <div className="grid-2">
          {data.cheat_sheet.map((item: any, idx: number) => (
            <div key={idx} className="panel" style={{ display: "flex", flexDirection: "column", gap: 8 }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <code style={{ fontSize: 15, fontWeight: 700, color: "var(--accent-cyan)", fontFamily: "var(--font-mono)" }}>
                  {item.fn}
                </code>
                <span className="tag tag-amber">{item.category}</span>
              </div>
              <MathText content={item.desc} />
              <CodeBlock code={item.example} language="matlab" label="Ejemplo MATLAB" />
            </div>
          ))}
        </div>
      )}

      {tab === "cuaderno" && (
        <div className="split-workspace" style={{ gridTemplateColumns: "290px minmax(0, 1fr)" }}>
          <div className="panel" style={{ padding: 12, display: "flex", flexDirection: "column", gap: 6 }}>
            <div style={{ fontSize: 11.5, fontFamily: "var(--font-mono)", color: "var(--text-muted)", padding: "4px 8px" }}>
              8 BLOQUES DE PRÁCTICAS (MPI1)
            </div>
            {data.guides.map((g: any) => (
              <button
                key={g.id}
                type="button"
                className={`choice-option ${selectedGuide === g.id ? "selected" : ""}`}
                onClick={() => setSelectedGuide(g.id)}
                style={{ padding: "9px 11px" }}
              >
                <span className="tag tag-blue" style={{ minWidth: 38, justifyContent: "center" }}>
                  {g.acronym}
                </span>
                <span style={{ fontSize: 13, fontWeight: 600 }}>{g.title}</span>
              </button>
            ))}
          </div>

          {activeGuide && (
            <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 14 }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 10 }}>
                <div>
                  <span className="tag tag-amber">Bloque {activeGuide.number} · {activeGuide.acronym}</span>
                  <h2 style={{ margin: "6px 0 0", fontSize: 19 }}>{activeGuide.title}</h2>
                </div>
                <button
                  type="button"
                  className="btn btn-sm btn-primary"
                  onClick={() => navigate("/ejercicios?topic=matlab")}
                >
                  <Terminal size={14} /> Probar reto de código
                </button>
              </div>
              <p style={{ margin: 0, color: "var(--text-secondary)", fontSize: 14 }}>{activeGuide.summary}</p>

              {activeGuide.code_examples.length > 0 && (
                <div>
                  <div style={{ fontSize: 13, fontWeight: 700, color: "var(--accent-cyan)", marginBottom: 6 }}>
                    Extractos de código del Live Script oficial:
                  </div>
                  {activeGuide.code_examples.map((code: string, i: number) => (
                    <CodeBlock key={i} code={code} language="matlab" label={`Script ${activeGuide.acronym} #${i + 1}`} />
                  ))}
                </div>
              )}

              <div
                style={{
                  borderTop: "1px solid var(--border-subtle)",
                  paddingTop: 14,
                  maxHeight: 520,
                  overflowY: "auto",
                }}
              >
                <div style={{ fontSize: 12, fontFamily: "var(--font-mono)", color: "var(--text-muted)", marginBottom: 8 }}>
                  GUION COMPLETO EXTRAÍDO DE 06_Practicas_MATLAB.md
                </div>
                <MathText content={activeGuide.content_md} />
              </div>
            </div>
          )}
        </div>
      )}

      {tab === "rubrica" && (
        <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          <h2 className="panel-title">
            <BookMarked size={17} style={{ color: "var(--accent-amber)" }} />
            Normas Obligatorias de Entrega Live Script (<code>Formato_practicas_Matlab_2026.pdf</code>)
          </h2>
          <p style={{ margin: 0, fontSize: 13.5, color: "var(--text-secondary)" }}>
            El incumplimiento de estas reglas resta nota directamente en las prácticas evaluables (SE2.1 = 40% de la asignatura). En las prácticas solo se permite MATLAB Copilot.
          </p>
          <div className="grid-2">
            {data.rubric_rules.map((r: any) => (
              <div
                key={r.num}
                style={{
                  padding: 14,
                  background: "var(--bg-inset)",
                  border: "1px solid var(--border-subtle)",
                  borderRadius: 8,
                  display: "flex",
                  gap: 12,
                }}
              >
                <CheckCircle2 size={18} style={{ color: "var(--accent-emerald)", flexShrink: 0, marginTop: 2 }} />
                <div>
                  <div style={{ fontWeight: 700, fontSize: 14, marginBottom: 4 }}>
                    Regla {r.num} · {r.title}
                  </div>
                  <MathText content={r.desc} />
                </div>
              </div>
            ))}
          </div>
          <CodeBlock
            label="Plantilla de cabecera ejemplar conforme a la rúbrica UFV"
            language="matlab"
            code={
              "clc, clear, clf\n" +
              "A = [2 2 4; 1 2 0; 1 3 1];\n" +
              "b = [2300; 800; 1500];\n" +
              "sol = A \\ b;\n" +
              "residuo = norm(A * sol - b);\n" +
              "fprintf('x1 = %6.2f uds | x2 = %6.2f uds | x3 = %6.2f uds (residuo = %.2e)\\n', sol(1), sol(2), sol(3), residuo)\n"
            }
          />
        </div>
      )}

      {tab === "practicas" && (
        <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          {data.evaluated_practices.map((pr: any, idx: number) => (
            <div key={idx} className="panel">
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 8 }}>
                <h3 style={{ margin: 0, fontSize: 16 }}>{pr.title}</h3>
                <span style={{ fontSize: 11.5, fontFamily: "var(--font-mono)", color: "var(--text-muted)" }}>
                  {pr.source}
                </span>
              </div>
              <div style={{ maxHeight: 360, overflowY: "auto" }}>
                <MathText content={pr.content_md} />
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
