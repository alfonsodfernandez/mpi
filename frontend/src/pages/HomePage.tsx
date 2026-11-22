import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { ArrowRight, BookOpen, Cpu, FileCheck2, Flame, Network, Terminal } from "lucide-react";
import { apiFetch } from "../api/client";

interface StudentOverview {
  display_name: string;
  total_active_seconds: number;
  today_active_seconds: number;
  total_sessions: number;
  streak_current: number;
  streak_best: number;
  exercises_completed: number;
  overall_accuracy: number;
  checklist_done: number;
  checklist_total: number;
  topic_mastery: { topic: string; label: string; total: number; correct: number; accuracy: number }[];
  recent_exams: {
    exam_id: string;
    mode: string;
    title: string;
    score_10: number;
    correct_count: number;
    total_questions: number;
    started_at: string;
    status: string;
  }[];
}

function fmtDuration(sec: number): string {
  const h = Math.floor(sec / 3600);
  const m = Math.floor((sec % 3600) / 60);
  if (h > 0) return `${h}h ${m}m`;
  return `${m} min`;
}

export const HomePage: React.FC = () => {
  const navigate = useNavigate();
  const [data, setData] = useState<StudentOverview | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    apiFetch<StudentOverview>("/api/student/overview")
      .then(setData)
      .catch(() => setData(null))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return <div className="panel">Cargando panel de estudio...</div>;
  }

  const checklistPct =
    data && data.checklist_total > 0
      ? Math.round((data.checklist_done / data.checklist_total) * 100)
      : 0;

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 22 }}>
      <div className="page-header">
        <div>
          <h1 className="page-title">Hola, {data?.display_name || "Pablo"}</h1>
          <p className="page-subtitle">
            Matemáticas para la Ingeniería I (UFV · Código 5666) · Estudia un poco cada día y entrena en Modo Blindado.
          </p>
        </div>
        <div style={{ display: "flex", gap: 10 }}>
          <button type="button" className="btn btn-primary" onClick={() => navigate("/ejercicios")}>
            <Cpu size={16} /> Entrenamiento Infinito
          </button>
          <button type="button" className="btn btn-secondary" onClick={() => navigate("/examenes")}>
            <FileCheck2 size={16} /> Simulacro UFV
          </button>
        </div>
      </div>

      {/* KPIs personales */}
      <div className="grid-4">
        <div className="kpi-card">
          <div className="kpi-label">Tiempo Efectivo Hoy</div>
          <div className="kpi-value">{fmtDuration(data?.today_active_seconds || 0)}</div>
          <div className="kpi-sub">Acumulado total: {fmtDuration(data?.total_active_seconds || 0)}</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-label">Racha de Estudio</div>
          <div className="kpi-value" style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <Flame size={22} style={{ color: "var(--accent-amber)" }} />
            {data?.streak_current || 0} días
          </div>
          <div className="kpi-sub">Mejor racha: {data?.streak_best || 0} días</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-label">Precisión en Ejercicios</div>
          <div className="kpi-value" style={{ color: (data?.overall_accuracy || 0) >= 70 ? "var(--accent-emerald)" : "var(--accent-cyan)" }}>
            {data?.overall_accuracy || 0}%
          </div>
          <div className="kpi-sub">{data?.exercises_completed || 0} ejercicios corregidos</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-label">Checklist del Temario</div>
          <div className="kpi-value">{checklistPct}%</div>
          <div className="kpi-sub">
            {data?.checklist_done || 0} / {data?.checklist_total || 30} competencias dominadas
          </div>
        </div>
      </div>

      {/* Accesos rápidos a módulos */}
      <div className="grid-2">
        <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          <h2 className="panel-title">Dominio por Bloques del Temario</h2>
          {(data?.topic_mastery || []).map((t) => {
            const color =
              t.total === 0
                ? "var(--border-strong)"
                : t.accuracy >= 75
                ? "var(--accent-emerald)"
                : t.accuracy >= 50
                ? "var(--accent-amber)"
                : "var(--accent-crimson)";
            return (
              <div key={t.topic} style={{ display: "flex", flexDirection: "column", gap: 5 }}>
                <div style={{ display: "flex", justifyContent: "space-between", fontSize: 13 }}>
                  <span style={{ fontWeight: 500 }}>{t.label}</span>
                  <span style={{ fontFamily: "var(--font-mono)", color: "var(--text-secondary)" }}>
                    {t.total > 0 ? `${t.accuracy}% (${t.correct}/${t.total})` : "Sin intentos"}
                  </span>
                </div>
                <div className="progress-track">
                  <div className="progress-fill" style={{ width: `${t.total > 0 ? Math.max(4, t.accuracy) : 0}%`, background: color }} />
                </div>
              </div>
            );
          })}
        </div>

        <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 12 }}>
          <h2 className="panel-title">Módulos de la Plataforma</h2>

          {[
            {
              icon: <BookOpen size={17} style={{ color: "var(--accent-cyan)" }} />,
              title: "Teoría Interactiva + Bloc de Notas",
              desc: "Guía docente, checklist oficial, definiciones, teoremas y pizarras resueltas de los 5 temas.",
              to: "/teoria",
            },
            {
              icon: <Cpu size={17} style={{ color: "var(--accent-amber)" }} />,
              title: "Motor de Ejercicios Infinitos (Lockdown)",
              desc: "26 generadores SymPy con variaciones únicas en cada intento, pizarra digital y corrección exacta.",
              to: "/ejercicios",
            },
            {
              icon: <Terminal size={17} style={{ color: "var(--accent-emerald)" }} />,
              title: "Laboratorio MATLAB + Retos de Código",
              desc: "Chuleta de funciones, rúbrica 2026, 8 cuadernos de prácticas (AR, DC, IP, FR, GR, LEO, MK, PR).",
              to: "/matlab",
            },
            {
              icon: <Network size={17} style={{ color: "var(--accent-blue)" }} />,
              title: "Proyecto 01 · Red Logística LOGISPAÑA",
              desc: "Simulador interactivo de grafo dirigido, Markov/PageRank, escenario DANA Valencia y defensa oral.",
              to: "/proyecto",
            },
          ].map((item) => (
            <button
              key={item.to}
              type="button"
              onClick={() => navigate(item.to)}
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                gap: 12,
                padding: "12px 14px",
                background: "var(--bg-inset)",
                border: "1px solid var(--border-subtle)",
                borderRadius: 8,
                cursor: "pointer",
                textAlign: "left",
                color: "var(--text-primary)",
              }}
            >
              <div style={{ display: "flex", gap: 12, alignItems: "flex-start" }}>
                <div style={{ marginTop: 2 }}>{item.icon}</div>
                <div>
                  <div style={{ fontWeight: 600, fontSize: 14 }}>{item.title}</div>
                  <div style={{ fontSize: 12.5, color: "var(--text-secondary)", marginTop: 2 }}>{item.desc}</div>
                </div>
              </div>
              <ArrowRight size={16} style={{ color: "var(--text-muted)", flexShrink: 0 }} />
            </button>
          ))}
        </div>
      </div>

      {/* Últimos simulacros */}
      {data && data.recent_exams.length > 0 && (
        <div className="panel">
          <h2 className="panel-title">Últimos Simulacros Realizados</h2>
          <div className="table-wrap">
            <table className="data-table">
              <thead>
                <tr>
                  <th>Fecha</th>
                  <th>Simulacro</th>
                  <th>Aciertos</th>
                  <th>Nota /10</th>
                  <th>Estado</th>
                </tr>
              </thead>
              <tbody>
                {data.recent_exams.map((ex) => (
                  <tr key={ex.exam_id}>
                    <td style={{ fontFamily: "var(--font-mono)", fontSize: 12 }}>
                      {new Date(ex.started_at).toLocaleString("es-ES")}
                    </td>
                    <td>{ex.title}</td>
                    <td style={{ fontFamily: "var(--font-mono)" }}>
                      {ex.correct_count}/{ex.total_questions}
                    </td>
                    <td>
                      <span className={`tag ${ex.score_10 >= 5 ? "tag-emerald" : "tag-crimson"}`}>
                        {ex.score_10.toFixed(2)} / 10
                      </span>
                    </td>
                    <td>{ex.status}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
};
