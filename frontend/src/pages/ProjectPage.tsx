import React, { useEffect, useState } from "react";
import { AlertTriangle, ChevronDown, ChevronRight, Network, ShieldAlert } from "lucide-react";
import { apiFetch } from "../api/client";
import { LogisticsGraph } from "../components/LogisticsGraph";
import { CodeBlock, MathText } from "../components/MathText";
import { LogisticsAnalysis } from "../types";

export const ProjectPage: React.FC = () => {
  const [hub, setHub] = useState<any>(null);
  const [analysis, setAnalysis] = useState<LogisticsAnalysis | null>(null);
  const [tab, setTab] = useState<"simulador" | "retos" | "defensa">("simulador");
  const [openOral, setOpenOral] = useState<Record<number, boolean>>({});

  useEffect(() => {
    apiFetch<any>("/api/content/project").then((res) => {
      setHub(res);
      setAnalysis(res.baseline_analysis);
    });
  }, []);

  const handleSimulateNode = async (disabledCenter: string | null) => {
    const q = disabledCenter ? `?disabled_center=${encodeURIComponent(disabledCenter)}` : "";
    const res = await apiFetch<LogisticsAnalysis>(`/api/content/project/simulate${q}`);
    setAnalysis(res);
  };

  if (!hub || !analysis) return <div className="panel">Calculando modelo de red logística con NumPy...</div>;

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
      <div className="page-header">
        <div>
          <h1 className="page-title">{hub.title}</h1>
          <p className="page-subtitle">
            Datos reales de <code>P01 Datos.xlsx</code> (12 centros, 22 rutas, histórico 2016–2025) · Simulación interactiva de los 6 Retos y escenario DANA Valencia.
          </p>
        </div>
      </div>

      {/* Rúbrica del proyecto */}
      <div className="grid-4">
        {hub.rubric_summary.map((r: any) => (
          <div key={r.item} className="kpi-card" style={{ padding: 14 }}>
            <div className="kpi-label">{r.weight}</div>
            <div style={{ fontSize: 13.5, fontWeight: 600, marginTop: 6 }}>{r.item}</div>
          </div>
        ))}
      </div>

      <div className="tabs">
        <button type="button" className={`tab-btn ${tab === "simulador" ? "active" : ""}`} onClick={() => setTab("simulador")}>
          Simulador Interactivo y DANA (Retos 1–6)
        </button>
        <button type="button" className={`tab-btn ${tab === "retos" ? "active" : ""}`} onClick={() => setTab("retos")}>
          Hoja de Ruta · 6 Retos + MATLAB
        </button>
        <button type="button" className={`tab-btn ${tab === "defensa" ? "active" : ""}`} onClick={() => setTab("defensa")}>
          Entrenador Defensa Oral (70%)
        </button>
      </div>

      {tab === "simulador" && (
        <>
          {analysis.disabled_center && (
            <div
              className="panel"
              style={{
                borderColor: "rgba(239, 68, 68, 0.45)",
                background: "rgba(239, 68, 68, 0.08)",
                display: "flex",
                alignItems: "center",
                gap: 12,
              }}
            >
              <ShieldAlert size={22} style={{ color: "#f87171", flexShrink: 0 }} />
              <div style={{ fontSize: 13.5 }}>
                <strong>Escenario de emergencia activo: {analysis.disabled_center} inoperativo.</strong> Se han interrumpido{" "}
                <strong>{analysis.summary.removed_routes_count} rutas</strong> ({analysis.summary.lost_weekly_tonnes} t/sem perdidas).{" "}
                {analysis.nodes.filter((n) => n.is_isolated).length > 0 && (
                  <>
                    Centros totalmente aislados:{" "}
                    <strong style={{ color: "#fbbf24" }}>
                      {analysis.nodes
                        .filter((n) => n.is_isolated)
                        .map((n) => n.name)
                        .join(", ")}
                    </strong>
                    .
                  </>
                )}
              </div>
            </div>
          )}

          <div style={{ display: "grid", gridTemplateColumns: "minmax(0, 1.02fr) minmax(0, 1.12fr)", gap: 18 }}>
            <div className="panel">
              <h2 className="panel-title">
                <Network size={17} style={{ color: "var(--accent-cyan)" }} /> Grafo Dirigido Ponderado (Retos 2 y 6)
              </h2>
              <LogisticsGraph analysis={analysis} onSelectDisabledCenter={handleSimulateNode} />
            </div>

            <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 14 }}>
              <h2 className="panel-title">Ranking Estructural PageRank y 4 Criterios (Retos 5–6)</h2>
              <div className="table-wrap" style={{ maxHeight: 450, overflowY: "auto" }}>
                <table className="data-table" style={{ fontSize: 12.5 }}>
                  <thead>
                    <tr>
                      <th style={{ padding: "8px 8px" }}>#</th>
                      <th style={{ padding: "8px 8px" }}>Centro</th>
                      <th style={{ padding: "8px 8px" }}>PageRank</th>
                      <th style={{ padding: "8px 8px" }}>Vol (t)</th>
                      <th style={{ padding: "8px 8px" }}>Grado</th>
                      <th style={{ padding: "8px 8px" }}>Interm.</th>
                      {analysis.disabled_center && <th style={{ padding: "8px 8px" }}>Δ Pos</th>}
                    </tr>
                  </thead>
                  <tbody>
                    {analysis.ranking_pagerank.map((n) => (
                      <tr key={n.name}>
                        <td style={{ fontFamily: "var(--font-mono)", fontWeight: 700 }}>{n.rank_now}</td>
                        <td>
                          <strong>{n.name}</strong>{" "}
                          {n.is_isolated && <span className="tag tag-amber">AISLADO</span>}
                        </td>
                        <td style={{ fontFamily: "var(--font-mono)", color: "var(--accent-cyan)", fontWeight: 600 }}>
                          {n.pagerank_pct.toFixed(2)}%
                        </td>
                        <td style={{ fontFamily: "var(--font-mono)" }}>{n.total_volume}</td>
                        <td style={{ fontFamily: "var(--font-mono)" }}>
                          {n.in_degree}↓ / {n.out_degree}↑
                        </td>
                        <td style={{ fontFamily: "var(--font-mono)" }}>{n.betweenness.toFixed(1)}</td>
                        {analysis.disabled_center && (
                          <td style={{ fontFamily: "var(--font-mono)" }}>
                            {n.rank_delta > 0 ? (
                              <span style={{ color: "var(--accent-emerald)" }}>▲ +{n.rank_delta}</span>
                            ) : n.rank_delta < 0 ? (
                              <span style={{ color: "var(--accent-crimson)" }}>▼ {n.rank_delta}</span>
                            ) : (
                              <span style={{ color: "var(--text-muted)" }}>—</span>
                            )}
                          </td>
                        )}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          <div className="grid-2">
            {/* Reto 1: Predicción 2028 */}
            <div className="panel">
              <h2 className="panel-title">Reto 1 · Ajuste Polinomial y Demanda 2028 (t = año − 2016)</h2>
              <div className="table-wrap">
                <table className="data-table">
                  <thead>
                    <tr>
                      <th>Grado</th>
                      <th>RMSE</th>
                      <th>Predicción 2028 (kt)</th>
                      <th>Δ vs 2025</th>
                    </tr>
                  </thead>
                  <tbody>
                    {analysis.demand.models.map((m) => (
                      <tr key={m.degree}>
                        <td style={{ fontFamily: "var(--font-mono)", fontWeight: 700 }}>Grado {m.degree}</td>
                        <td style={{ fontFamily: "var(--font-mono)" }}>{m.rmse.toFixed(4)}</td>
                        <td style={{ fontFamily: "var(--font-mono)", color: "var(--accent-cyan)", fontWeight: 600 }}>
                          {m.prediction_2028.toFixed(2)} kt
                        </td>
                        <td style={{ fontFamily: "var(--font-mono)", color: "var(--accent-emerald)" }}>
                          +{m.pct_increase_vs_2025.toFixed(2)}%
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Reto 4: 3 Métodos de Equilibrio Markov */}
            <div className="panel">
              <h2 className="panel-title">Reto 4 · Validación de 3 Métodos Markov (Error &lt; 10⁻¹²)</h2>
              <div className="table-wrap">
                <table className="data-table">
                  <thead>
                    <tr>
                      <th>Método Matemático</th>
                      <th>Iteraciones</th>
                      <th>Norma Residuo ‖Pπ − π‖₂</th>
                    </tr>
                  </thead>
                  <tbody>
                    {analysis.markov_methods.map((mm) => (
                      <tr key={mm.method}>
                        <td>{mm.method}</td>
                        <td style={{ fontFamily: "var(--font-mono)" }}>{mm.iterations}</td>
                        <td style={{ fontFamily: "var(--font-mono)", color: "var(--accent-emerald)" }}>
                          {mm.residual_norm.toExponential(2)}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </>
      )}

      {tab === "retos" && (
        <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          {hub.retos.map((r: any) => (
            <div key={r.id} className="panel" style={{ display: "flex", flexDirection: "column", gap: 10 }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 8 }}>
                <h2 style={{ margin: 0, fontSize: 17 }}>{r.title}</h2>
                <span className="tag tag-amber">Peso: {r.weight}</span>
              </div>
              <MathText content={r.math_core} />
              <ul style={{ margin: "4px 0 6px 20px", padding: 0, display: "flex", flexDirection: "column", gap: 5, fontSize: 13.5 }}>
                {r.objectives.map((o: string, i: number) => (
                  <li key={i}>{o}</li>
                ))}
              </ul>
              <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
                {r.matlab_functions.map((fn: string) => (
                  <span key={fn} className="tag tag-blue">
                    {fn}()
                  </span>
                ))}
              </div>
              <div
                style={{
                  padding: "10px 12px",
                  background: "var(--bg-inset)",
                  borderLeft: "3px solid var(--accent-amber)",
                  borderRadius: "0 6px 6px 0",
                  fontSize: 13,
                }}
              >
                <strong>Clave técnica:</strong> <MathText content={r.template_hint} />
              </div>
            </div>
          ))}
          <CodeBlock
            label="Importación obligatoria de datos desde P01 Datos.xlsx (MATLAB)"
            language="matlab"
            code={
              "clc, clear, clf\n" +
              "T_centros = readtable('P01 Datos.xlsx', 'Sheet', 'centros de distribución');\n" +
              "T_flujos  = readtable('P01 Datos.xlsx', 'Sheet', 'flujos semanales');\n" +
              "T_vol     = readtable('P01 Datos.xlsx', 'Sheet', 'volumen de mercancías');\n" +
              "G = digraph(T_flujos.Origen, T_flujos.Destino, T_flujos.Flujo);\n" +
              "A = full(adjacency(G, 'weighted'));\n"
            }
          />
        </div>
      )}

      {tab === "defensa" && (
        <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
            <AlertTriangle size={20} style={{ color: "var(--accent-amber)" }} />
            <div>
              <h2 style={{ margin: 0, fontSize: 17 }}>Preparación de la Defensa Oral Individual (70% de la Presentación)</h2>
              <p style={{ margin: "2px 0 0", fontSize: 13, color: "var(--text-secondary)" }}>
                El profesor puede preguntar por cualquier reto o función MATLAB independientemente de qué parte redactaras en tu grupo. Intenta responder en voz alta antes de desplegar la respuesta.
              </p>
            </div>
          </div>

          {hub.oral_defense_questions.map((item: any, idx: number) => {
            const isOpen = !!openOral[idx];
            return (
              <div
                key={idx}
                style={{
                  background: "var(--bg-inset)",
                  border: "1px solid var(--border-subtle)",
                  borderRadius: 8,
                  padding: 14,
                }}
              >
                <div style={{ fontWeight: 700, fontSize: 14.5, marginBottom: 10 }}>
                  {idx + 1}. {item.q}
                </div>
                <button
                  type="button"
                  className="btn btn-sm btn-secondary"
                  onClick={() => setOpenOral((p) => ({ ...p, [idx]: !isOpen }))}
                >
                  {isOpen ? <ChevronDown size={14} /> : <ChevronRight size={14} />}
                  {isOpen ? "Ocultar respuesta modelo" : "Comprobar respuesta modelo"}
                </button>
                {isOpen && (
                  <div style={{ marginTop: 10, paddingTop: 10, borderTop: "1px solid var(--border-subtle)" }}>
                    <MathText content={item.a} />
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
