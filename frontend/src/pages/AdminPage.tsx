import React, { useCallback, useEffect, useState } from "react";
import {
  Activity,
  AlertTriangle,
  Download,
  RefreshCw,
  ShieldAlert,
  TrendingDown,
} from "lucide-react";
import { apiFetch, downloadAdminExport } from "../api/client";

function fmtSeconds(sec: number | null | undefined): string {
  const s = sec || 0;
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const rem = s % 60;
  if (h > 0) return `${h}h ${m}m`;
  if (m > 0) return `${m}m ${rem}s`;
  return `${rem}s`;
}

export const AdminPage: React.FC = () => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [violationFilter, setViolationFilter] = useState<string>("all");
  const [tab, setTab] = useState<"resumen" | "infracciones" | "sesiones" | "examenes">("resumen");

  const loadDashboard = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await apiFetch<any>("/api/admin/dashboard");
      setData(res);
    } catch (err: any) {
      setError(err?.message || "No se pudo cargar el panel de administración.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadDashboard();
    const id = window.setInterval(() => {
      void apiFetch<any>("/api/admin/dashboard").then(setData).catch(() => {});
    }, 30000);
    return () => window.clearInterval(id);
  }, [loadDashboard]);

  if (loading && !data) return <div className="panel">Cargando telemetría y analítica académica de Pablo...</div>;
  if (error) return <div className="panel" style={{ color: "#fca5a5" }}>{error}</div>;
  if (!data) return null;

  const kpis = data.kpis || {};
  const live = data.student?.live_session;
  const violations: any[] = data.violations || [];
  const filteredViolations = violations.filter(
    (v) => violationFilter === "all" || v.violation_type === violationFilter || v.severity === violationFilter
  );

  // Escala del gráfico diario 14 días
  const daily: any[] = data.daily_activity || [];
  const maxMin = Math.max(10, ...daily.map((d) => d.active_minutes));

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 22 }}>
      <div className="page-header">
        <div>
          <div style={{ display: "flex", alignItems: "center", gap: 10, flexWrap: "wrap" }}>
            <h1 className="page-title">Panel de Auditoría y Control · {data.student?.display_name || "Pablo"}</h1>
            {live ? (
              <span className="tag tag-emerald">
                <Activity size={12} /> EN LÍNEA AHORA · vista: {live.current_view} ({live.ip_address})
              </span>
            ) : (
              <span className="tag">Desconectado</span>
            )}
          </div>
          <p className="page-subtitle">
            Monitorización en tiempo real de sesiones, tiempo activo efectivo, infracciones anti-trampas y dominio académico.
          </p>
        </div>

        <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
          <button type="button" className="btn btn-secondary btn-sm" onClick={loadDashboard}>
            <RefreshCw size={14} /> Actualizar
          </button>
          <button type="button" className="btn btn-primary btn-sm" onClick={() => downloadAdminExport("csv", "all")}>
            <Download size={14} /> Exportar CSV Completo
          </button>
          <button type="button" className="btn btn-secondary btn-sm" onClick={() => downloadAdminExport("json", "all")}>
            <Download size={14} /> Exportar JSON
          </button>
        </div>
      </div>

      {/* KPIs principales */}
      <div className="grid-4">
        <div className="kpi-card">
          <div className="kpi-label">Accesos Totales</div>
          <div className="kpi-value">{kpis.total_accesses || 0}</div>
          <div className="kpi-sub">Racha actual: {kpis.streak_current_days || 0}d (mejor: {kpis.streak_best_days || 0}d)</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-label">Tiempo Efectivo Activo</div>
          <div className="kpi-value" style={{ color: "var(--accent-cyan)" }}>
            {fmtSeconds(kpis.total_active_seconds)}
          </div>
          <div className="kpi-sub">Tiempo sesión total (incl. inactividad): {fmtSeconds(kpis.total_wall_seconds)}</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-label">Rendimiento Académico</div>
          <div className="kpi-value" style={{ color: (kpis.overall_accuracy_pct || 0) >= 65 ? "var(--accent-emerald)" : "var(--accent-amber)" }}>
            {kpis.overall_accuracy_pct || 0}%
          </div>
          <div className="kpi-sub">
            {kpis.total_questions_answered || 0} preguntas · media {kpis.avg_seconds_per_question || 0}s/preg
          </div>
        </div>
        <div className="kpi-card" style={{ borderColor: (kpis.total_violations || 0) > 0 ? "rgba(239, 68, 68, 0.45)" : undefined }}>
          <div className="kpi-label">Infracciones Anti-Trampas</div>
          <div className="kpi-value" style={{ color: (kpis.total_violations || 0) > 0 ? "var(--accent-crimson)" : "var(--accent-emerald)" }}>
            {kpis.total_violations || 0}
          </div>
          <div className="kpi-sub">
            Graves (reinicio forzado): {kpis.high_severity_violations || 0} · Simulacros inv.: {kpis.exams_invalidated || 0}
          </div>
        </div>
      </div>

      <div className="tabs">
        <button type="button" className={`tab-btn ${tab === "resumen" ? "active" : ""}`} onClick={() => setTab("resumen")}>
          Analítica Académica y Puntos Débiles
        </button>
        <button type="button" className={`tab-btn ${tab === "infracciones" ? "active" : ""}`} onClick={() => setTab("infracciones")}>
          Log Anti-Trampas ({violations.length})
        </button>
        <button type="button" className={`tab-btn ${tab === "sesiones" ? "active" : ""}`} onClick={() => setTab("sesiones")}>
          Registro de Sesiones ({(data.sessions || []).length})
        </button>
        <button type="button" className={`tab-btn ${tab === "examenes" ? "active" : ""}`} onClick={() => setTab("examenes")}>
          Simulacros y Ejercicios ({(data.exams || []).length})
        </button>
      </div>

      {tab === "resumen" && (
        <>
          <div className="grid-2">
            {/* Analítica por tema */}
            <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 14 }}>
              <h2 className="panel-title">Precisión y Tiempo Medio por Tema</h2>
              <div className="table-wrap">
                <table className="data-table">
                  <thead>
                    <tr>
                      <th>Tema</th>
                      <th>Intentos</th>
                      <th>% Acierto</th>
                      <th>T. Medio</th>
                      <th>Timeouts</th>
                    </tr>
                  </thead>
                  <tbody>
                    {(data.topic_analytics || []).map((t: any) => (
                      <tr key={t.topic}>
                        <td style={{ fontWeight: 600 }}>{t.label}</td>
                        <td style={{ fontFamily: "var(--font-mono)" }}>
                          {t.correct}/{t.attempts}
                        </td>
                        <td>
                          <span
                            className={`tag ${
                              t.attempts === 0
                                ? ""
                                : t.accuracy_pct >= 75
                                ? "tag-emerald"
                                : t.accuracy_pct >= 50
                                ? "tag-amber"
                                : "tag-crimson"
                            }`}
                          >
                            {t.accuracy_pct}%
                          </span>
                        </td>
                        <td style={{ fontFamily: "var(--font-mono)" }}>{t.avg_seconds}s</td>
                        <td style={{ fontFamily: "var(--font-mono)", color: t.timeouts > 0 ? "var(--accent-amber)" : "var(--text-muted)" }}>
                          {t.timeouts}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
              <div style={{ fontSize: 12.5, color: "var(--text-secondary)" }}>
                Checklist oficial dominado: <strong>{kpis.checklist_done || 0} / {kpis.checklist_total || 30}</strong> competencias ·
                Nota media en simulacros: <strong>{kpis.avg_exam_score_10 || 0} / 10</strong> ·
                Temas con apuntes propios: <strong>{data.notes_count || 0}</strong>.
              </div>
            </div>

            {/* Detector automático de puntos débiles */}
            <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 12 }}>
              <h2 className="panel-title">
                <TrendingDown size={17} style={{ color: "var(--accent-amber)" }} /> Detección Automática de Puntos Débiles
              </h2>
              {(data.weak_spots || []).length === 0 ? (
                <p style={{ color: "var(--text-secondary)", fontSize: 13.5 }}>
                  No se detectan puntos débiles críticos por debajo del 70% todavía (o faltan intentos suficientes).
                </p>
              ) : (
                (data.weak_spots || []).map((w: any) => (
                  <div
                    key={w.generator_id}
                    style={{
                      padding: 12,
                      background: "var(--bg-inset)",
                      borderLeft: `3px solid ${w.accuracy_pct < 50 ? "var(--accent-crimson)" : "var(--accent-amber)"}`,
                      borderRadius: "0 8px 8px 0",
                    }}
                  >
                    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", gap: 8 }}>
                      <strong style={{ fontSize: 13.5 }}>{w.label}</strong>
                      <span className={`tag ${w.accuracy_pct < 50 ? "tag-crimson" : "tag-amber"}`}>
                        {w.accuracy_pct}% ({w.attempts} int.)
                      </span>
                    </div>
                    <div style={{ fontSize: 12, color: "var(--text-muted)", marginTop: 2 }}>{w.topic_label}</div>
                    <div style={{ fontSize: 12.5, color: "var(--text-secondary)", marginTop: 6 }}>{w.recommendation}</div>
                  </div>
                ))
              )}
            </div>
          </div>

          {/* Gráfico de actividad diaria 14 días */}
          <div className="panel">
            <h2 className="panel-title">Actividad Diaria Efectiva (Últimos 14 Días · Minutos Activos)</h2>
            <div style={{ display: "grid", gridTemplateColumns: "repeat(14, minmax(0, 1fr))", gap: 6, alignItems: "end", height: 150, paddingTop: 18 }}>
              {daily.map((d) => {
                const barH = Math.max(4, Math.round((d.active_minutes / maxMin) * 105));
                return (
                  <div
                    key={d.date}
                    title={`${d.date}: ${d.active_minutes} min activos · ${d.exercises} ejerc. · ${d.violations} infracc.`}
                    style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 6 }}
                  >
                    <span style={{ fontSize: 10, fontFamily: "var(--font-mono)", color: "var(--text-muted)" }}>
                      {d.active_minutes > 0 ? `${Math.round(d.active_minutes)}m` : ""}
                    </span>
                    <div
                      style={{
                        width: "100%",
                        maxWidth: 32,
                        height: barH,
                        borderRadius: "4px 4px 2px 2px",
                        background: d.violations > 0 ? "var(--accent-crimson)" : d.active_minutes > 0 ? "var(--accent-cyan)" : "var(--bg-elevated)",
                      }}
                    />
                    <span style={{ fontSize: 10, fontFamily: "var(--font-mono)", color: "var(--text-muted)" }}>
                      {d.date.slice(5)}
                    </span>
                  </div>
                );
              })}
            </div>
          </div>
        </>
      )}

      {tab === "infracciones" && (
        <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 10 }}>
            <h2 className="panel-title" style={{ margin: 0 }}>
              <ShieldAlert size={18} style={{ color: "var(--accent-crimson)" }} /> Registro Completo de Infracciones Anti-Trampas
            </h2>
            <div style={{ display: "flex", gap: 8 }}>
              <select className="select" style={{ width: 220 }} value={violationFilter} onChange={(e) => setViolationFilter(e.target.value)}>
                <option value="all">Todas las infracciones</option>
                <option value="high">Solo severidad ALTA (Reinicio)</option>
                <option value="EXIT_FULLSCREEN">Salida de pantalla completa</option>
                <option value="TAB_SWITCH">Cambio de pestaña</option>
                <option value="WINDOW_BLUR">Pérdida de foco (Alt+Tab)</option>
                <option value="DEVTOOLS_ATTEMPT">Intento DevTools / F12</option>
                <option value="COPY_ATTEMPT">Intento copiar / pegar</option>
              </select>
              <button type="button" className="btn btn-sm btn-secondary" onClick={() => downloadAdminExport("csv", "violations")}>
                <Download size={13} /> CSV Infracciones
              </button>
            </div>
          </div>

          {filteredViolations.length === 0 ? (
            <p style={{ color: "var(--accent-emerald)", fontSize: 13.5 }}>Sin infracciones registradas para este filtro.</p>
          ) : (
            <div className="table-wrap">
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Fecha y Hora</th>
                    <th>Tipo</th>
                    <th>Modo / Tema</th>
                    <th>Pregunta</th>
                    <th>Reinicio</th>
                    <th>IP</th>
                    <th>Detalle</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredViolations.map((v) => (
                    <tr key={v.id}>
                      <td style={{ fontFamily: "var(--font-mono)", fontSize: 12 }}>
                        {new Date(v.created_at).toLocaleString("es-ES")}
                      </td>
                      <td>
                        <span className={`tag ${v.severity === "high" ? "tag-crimson" : "tag-amber"}`}>
                          {v.violation_type}
                        </span>
                      </td>
                      <td>
                        <div style={{ fontWeight: 600, fontSize: 12.5 }}>{v.context_mode.toUpperCase()}</div>
                        <div style={{ fontSize: 11.5, color: "var(--text-muted)" }}>{v.topic_label}</div>
                      </td>
                      <td style={{ fontSize: 12.5 }}>{v.question_ref}</td>
                      <td>
                        {v.triggered_reset ? (
                          <span className="tag tag-crimson">SÍ</span>
                        ) : (
                          <span className="tag">Bloqueado</span>
                        )}
                      </td>
                      <td style={{ fontFamily: "var(--font-mono)", fontSize: 12 }}>{v.ip_address}</td>
                      <td style={{ fontSize: 12, color: "var(--text-secondary)" }}>{v.details}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}

      {tab === "sesiones" && (
        <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 10 }}>
            <h2 className="panel-title" style={{ margin: 0 }}>Registro de Sesiones, IP y Dispositivos</h2>
            <button type="button" className="btn btn-sm btn-secondary" onClick={() => downloadAdminExport("csv", "sessions")}>
              <Download size={13} /> CSV Sesiones
            </button>
          </div>
          <div className="table-wrap">
            <table className="data-table">
              <thead>
                <tr>
                  <th>Inicio</th>
                  <th>Última Actividad / Fin</th>
                  <th>IP</th>
                  <th>Dispositivo / Navegador</th>
                  <th>Duración Total</th>
                  <th>Tiempo Activo Real</th>
                  <th>Estado</th>
                </tr>
              </thead>
              <tbody>
                {(data.sessions || []).map((s: any) => (
                  <tr key={s.id}>
                    <td style={{ fontFamily: "var(--font-mono)", fontSize: 12 }}>
                      {new Date(s.started_at).toLocaleString("es-ES")}
                    </td>
                    <td style={{ fontFamily: "var(--font-mono)", fontSize: 12 }}>
                      {new Date(s.ended_at || s.last_seen_at).toLocaleString("es-ES")}
                    </td>
                    <td style={{ fontFamily: "var(--font-mono)", fontSize: 12 }}>{s.ip_address}</td>
                    <td title={s.user_agent}>{s.device_summary}</td>
                    <td style={{ fontFamily: "var(--font-mono)" }}>{fmtSeconds(s.wall_seconds)}</td>
                    <td style={{ fontFamily: "var(--font-mono)", color: "var(--accent-cyan)", fontWeight: 600 }}>
                      {fmtSeconds(s.active_seconds)}
                    </td>
                    <td>
                      {s.is_online ? (
                        <span className="tag tag-emerald">Online ({s.current_view})</span>
                      ) : (
                        <span className="tag">Finalizada</span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {tab === "examenes" && (
        <div style={{ display: "flex", flexDirection: "column", gap: 18 }}>
          <div className="panel">
            <h2 className="panel-title">Historial de Exámenes Simulados</h2>
            <div className="table-wrap">
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Fecha</th>
                    <th>Simulacro</th>
                    <th>Estado</th>
                    <th>Nota /10</th>
                    <th>Aciertos</th>
                    <th>Tiempo</th>
                  </tr>
                </thead>
                <tbody>
                  {(data.exams || []).map((e: any) => (
                    <tr key={e.exam_id}>
                      <td style={{ fontFamily: "var(--font-mono)", fontSize: 12 }}>
                        {new Date(e.started_at).toLocaleString("es-ES")}
                      </td>
                      <td>{e.title}</td>
                      <td>
                        {e.status === "invalidated" ? (
                          <span className="tag tag-crimson">
                            <AlertTriangle size={11} /> {e.invalidation_reason || "Invalidado"}
                          </span>
                        ) : e.status === "timeout" ? (
                          <span className="tag tag-amber">Timeout</span>
                        ) : (
                          <span className="tag tag-emerald">Completado</span>
                        )}
                      </td>
                      <td style={{ fontFamily: "var(--font-mono)", fontWeight: 700 }}>
                        {e.status === "invalidated" ? "—" : `${e.score_10.toFixed(2)} / 10`}
                      </td>
                      <td style={{ fontFamily: "var(--font-mono)" }}>
                        {e.correct_count}/{e.total_questions}
                      </td>
                      <td style={{ fontFamily: "var(--font-mono)" }}>{fmtSeconds(e.time_spent_seconds)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          <div className="panel">
            <h2 className="panel-title">Últimos Ejercicios Procedurales</h2>
            <div className="table-wrap">
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Fecha</th>
                    <th>Tema</th>
                    <th>Ejercicio</th>
                    <th>Estado</th>
                    <th>Tiempo</th>
                  </tr>
                </thead>
                <tbody>
                  {(data.recent_exercises || []).map((a: any) => (
                    <tr key={a.attempt_id}>
                      <td style={{ fontFamily: "var(--font-mono)", fontSize: 12 }}>
                        {new Date(a.started_at).toLocaleString("es-ES")}
                      </td>
                      <td>{a.topic_label}</td>
                      <td>{a.title}</td>
                      <td>
                        {a.status === "invalidated" ? (
                          <span className="tag tag-crimson">Invalidado</span>
                        ) : a.status === "timeout" ? (
                          <span className="tag tag-amber">Timeout</span>
                        ) : a.is_correct ? (
                          <span className="tag tag-emerald">Correcto</span>
                        ) : (
                          <span className="tag tag-crimson">Fallado ({Math.round(a.score * 100)}%)</span>
                        )}
                      </td>
                      <td style={{ fontFamily: "var(--font-mono)" }}>{fmtSeconds(a.time_spent_seconds)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
