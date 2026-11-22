import React, { useCallback, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  CheckCircle2,
  ChevronLeft,
  ChevronRight,
  Cpu,
  FileCheck2,
  Send,
  Shield,
  Timer,
  XCircle,
} from "lucide-react";
import { apiFetch } from "../api/client";
import { AnswerInput, createInitialAnswer } from "../components/AnswerInput";
import {
  BreachInfo,
  enterFullscreenSafely,
  exitFullscreenSafely,
  LockdownBreachOverlay,
  LockdownRulesModal,
  useLockdownGuardian,
} from "../components/LockdownGuard";
import { MathText } from "../components/MathText";
import { ProtectedPrompt } from "../components/ProtectedPrompt";
import { Scratchpad } from "../components/Scratchpad";
import { ActiveExam, ExamResult, UserInfo } from "../types";

function fmtExamClock(sec: number): string {
  const s = Math.max(0, sec);
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const r = s % 60;
  if (h > 0) {
    return `${String(h).padStart(2, "0")}:${String(m).padStart(2, "0")}:${String(r).padStart(2, "0")}`;
  }
  return `${String(m).padStart(2, "0")}:${String(r).padStart(2, "0")}`;
}

export const ExamPage: React.FC<{ user: UserInfo }> = ({ user }) => {
  const navigate = useNavigate();
  const [modes, setModes] = useState<any[]>([]);
  const [history, setHistory] = useState<any[]>([]);
  const [bankData, setBankData] = useState<any>(null);
  const [bankFilter, setBankFilter] = useState<string>("all");
  const [pageTab, setPageTab] = useState<"simulador" | "banco" | "practicos">("simulador");

  // Modal y examen en curso
  const [pendingMode, setPendingMode] = useState<any | null>(null);
  const [modalError, setModalError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const [exam, setExam] = useState<ActiveExam | null>(null);
  const [currentIdx, setCurrentIdx] = useState(0);
  const [answersMap, setAnswersMap] = useState<Record<string, any>>({});
  const [secondsLeft, setSecondsLeft] = useState(0);
  const [submitting, setSubmitting] = useState(false);

  const [result, setResult] = useState<ExamResult | null>(null);
  const [breach, setBreach] = useState<BreachInfo | null>(null);
  const [minorToast, setMinorToast] = useState<string | null>(null);

  const loadData = useCallback(() => {
    apiFetch<{ modes: any[] }>("/api/exams/modes").then((r) => setModes(r.modes));
    apiFetch<{ exams: any[] }>("/api/exams/history").then((r) => setHistory(r.exams));
    apiFetch<any>("/api/content/exam-bank").then(setBankData);
  }, []);

  useEffect(() => {
    loadData();
  }, [loadData]);

  const startFreshExam = useCallback(async (mode: string) => {
    const ex = await apiFetch<ActiveExam>("/api/exams/start", {
      method: "POST",
      body: JSON.stringify({ mode }),
    });
    const initAnswers: Record<string, any> = {};
    ex.questions.forEach((q) => {
      initAnswers[q.question_id] = createInitialAnswer(q.prompt.input_spec);
    });
    setExam(ex);
    setAnswersMap(initAnswers);
    setCurrentIdx(0);
    setSecondsLeft(ex.time_limit_seconds);
    setResult(null);
  }, []);

  const handleConfirmStart = async () => {
    if (!pendingMode) return;
    setModalError(null);
    setLoading(true);
    const fsOk = await enterFullscreenSafely();
    if (!fsOk) {
      setModalError("Debes aceptar Pantalla Completa para iniciar el simulacro de examen.");
      setLoading(false);
      return;
    }
    try {
      await startFreshExam(pendingMode.mode);
      setPendingMode(null);
    } catch (err: any) {
      setModalError(err?.message || "No se pudo iniciar el simulacro.");
      await exitFullscreenSafely();
    } finally {
      setLoading(false);
    }
  };

  const handleFinalizeExam = useCallback(
    async (timedOut: boolean = false) => {
      if (!exam || submitting) return;
      setSubmitting(true);
      try {
        const res = await apiFetch<ExamResult>(`/api/exams/${exam.exam_id}/finalize`, {
          method: "POST",
          body: JSON.stringify({ timed_out: timedOut, answers: answersMap }),
        });
        setResult(res);
        setExam(null);
        await exitFullscreenSafely();
        loadData();
      } catch (err: any) {
        setMinorToast(err?.message || "Error al finalizar el simulacro.");
      } finally {
        setSubmitting(false);
      }
    },
    [exam, submitting, answersMap, loadData]
  );

  // Temporizador global estricto del examen
  useEffect(() => {
    if (!exam || breach) return;
    const t = window.setInterval(() => {
      setSecondsLeft((prev) => {
        if (prev <= 1) {
          window.clearInterval(t);
          void handleFinalizeExam(true);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => window.clearInterval(t);
  }, [exam, breach, handleFinalizeExam]);

  const currentQuestion = exam ? exam.questions[currentIdx] : null;

  // Guardián anti-trampas en todo el examen
  const { triggerMinor } = useLockdownGuardian({
    active: Boolean(exam && !breach),
    contextMode: "exam",
    topic: currentQuestion?.topic || "examen",
    questionRef: currentQuestion ? `P${currentQuestion.question_index}: ${currentQuestion.title}` : "Simulacro",
    activeExamId: exam?.exam_id,
    onMajorBreach: (info) => {
      const prevMode = exam?.mode || "express";
      setBreach(info);
      setExam(null);
      setPendingMode(modes.find((m) => m.mode === prevMode) || { mode: prevMode });
      loadData();
    },
    onMinorWarning: (msg) => {
      setMinorToast(msg);
      window.setTimeout(() => setMinorToast(null), 4500);
    },
  });

  const handleAnswerChange = (qid: string, val: any) => {
    setAnswersMap((prev) => ({ ...prev, [qid]: val }));
    if (exam) {
      void apiFetch(`/api/exams/${exam.exam_id}/questions/${qid}`, {
        method: "PUT",
        body: JSON.stringify({ answer: val }),
      }).catch(() => {});
    }
  };

  const handleRestartAfterBreach = async () => {
    setLoading(true);
    const fsOk = await enterFullscreenSafely();
    if (!fsOk) {
      setLoading(false);
      return;
    }
    try {
      const m = pendingMode?.mode || "express";
      setBreach(null);
      setPendingMode(null);
      await startFreshExam(m);
    } finally {
      setLoading(false);
    }
  };

  const handleReviewPastExam = async (examId: string) => {
    const rev = await apiFetch<ExamResult>(`/api/exams/${examId}/review`);
    setResult(rev);
  };

  // 1. Vista Examen Activo en Modo Blindado
  if (exam || breach) {
    const pctLeft = exam ? secondsLeft / Math.max(1, exam.time_limit_seconds) : 1;
    const timerClass = pctLeft <= 0.1 ? "critical" : pctLeft <= 0.25 ? "warn" : "";

    return (
      <div style={{ minHeight: "100vh", background: "var(--bg-canvas)" }}>
        {breach && (
          <LockdownBreachOverlay
            breach={breach}
            onRestart={handleRestartAfterBreach}
            onExit={async () => {
              setBreach(null);
              setPendingMode(null);
              await exitFullscreenSafely();
            }}
            restarting={loading}
          />
        )}
        {minorToast && <div className="toast-alert">{minorToast}</div>}

        {exam && currentQuestion && (
          <>
            <div className="lockdown-bar">
              <div style={{ display: "flex", alignItems: "center", gap: 10, flexWrap: "wrap" }}>
                <span className="tag tag-crimson">
                  <Shield size={12} /> SIMULACRO BLINDADO
                </span>
                <span style={{ fontWeight: 700, fontSize: 14 }}>{exam.title}</span>
                <span className="tag tag-blue">
                  Pregunta {currentQuestion.question_index} / {exam.total_questions} ({currentQuestion.points_weight} ptos)
                </span>
              </div>
              <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
                  <Timer size={16} style={{ color: "var(--text-muted)" }} />
                  <div className={`lockdown-timer ${timerClass}`}>{fmtExamClock(secondsLeft)}</div>
                </div>
                <button
                  type="button"
                  className="btn btn-emerald btn-sm"
                  onClick={() => handleFinalizeExam(false)}
                  disabled={submitting}
                >
                  <Send size={14} /> {submitting ? "Corrigiendo..." : "Entregar Examen"}
                </button>
              </div>
            </div>

            <div style={{ maxWidth: 1420, margin: "0 auto", padding: "18px 26px 48px" }}>
              {/* Navegador de preguntas */}
              <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: 18 }}>
                {exam.questions.map((q, idx) => {
                  const rawAns = answersMap[q.question_id];
                  const hasAnswer =
                    rawAns !== "" &&
                    rawAns !== null &&
                    JSON.stringify(rawAns).replace(/[\[\]{}":,null\s]/g, "").length > 0;
                  const isCurr = idx === currentIdx;
                  return (
                    <button
                      key={q.question_id}
                      type="button"
                      className={`btn btn-sm ${isCurr ? "btn-primary" : hasAnswer ? "btn-emerald" : "btn-secondary"}`}
                      onClick={() => setCurrentIdx(idx)}
                      style={{ minWidth: 44 }}
                    >
                      P{q.question_index}
                    </button>
                  );
                })}
              </div>

              <div className="split-workspace">
                <div style={{ display: "flex", flexDirection: "column", gap: 18 }}>
                  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                    <span className="tag">{currentQuestion.topic_label}</span>
                    <span style={{ fontSize: 12.5, color: "var(--text-secondary)" }}>
                      Peso en examen: <strong>{currentQuestion.points_weight} ptos</strong>
                    </span>
                  </div>

                  <ProtectedPrompt
                    prompt={currentQuestion.prompt}
                    studentName={user.display_name}
                    watermarkBase={exam.watermark_text}
                    onBlockedAction={(t, d) => triggerMinor(t, d)}
                  />

                  <div className="panel">
                    <h3 className="panel-title">Respuesta · Pregunta {currentQuestion.question_index}</h3>
                    <AnswerInput
                      spec={currentQuestion.prompt.input_spec}
                      value={answersMap[currentQuestion.question_id]}
                      onChange={(val) => handleAnswerChange(currentQuestion.question_id, val)}
                    />
                    <div style={{ display: "flex", justifyContent: "space-between", marginTop: 18 }}>
                      <button
                        type="button"
                        className="btn btn-secondary"
                        disabled={currentIdx === 0}
                        onClick={() => setCurrentIdx((i) => Math.max(0, i - 1))}
                      >
                        <ChevronLeft size={15} /> Anterior
                      </button>
                      {currentIdx < exam.questions.length - 1 ? (
                        <button
                          type="button"
                          className="btn btn-primary"
                          onClick={() => setCurrentIdx((i) => Math.min(exam.questions.length - 1, i + 1))}
                        >
                          Siguiente <ChevronRight size={15} />
                        </button>
                      ) : (
                        <button
                          type="button"
                          className="btn btn-emerald"
                          onClick={() => handleFinalizeExam(false)}
                          disabled={submitting}
                        >
                          <Send size={15} /> Finalizar y Corregir Examen
                        </button>
                      )}
                    </div>
                  </div>
                </div>

                <div style={{ position: "sticky", top: 76 }}>
                  <Scratchpad />
                </div>
              </div>
            </div>
          </>
        )}
      </div>
    );
  }

  // 2. Vista Revisión Post-Examen
  if (result) {
    const passed = result.score_10 >= 5.0;
    return (
      <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
        <div className="page-header">
          <div>
            <h1 className="page-title">Corrección del Simulacro</h1>
            <p className="page-subtitle">{result.title}</p>
          </div>
          <button type="button" className="btn btn-secondary" onClick={() => setResult(null)}>
            Volver al Simulador
          </button>
        </div>

        <div className="grid-4">
          <div className="kpi-card">
            <div className="kpi-label">Calificación Final</div>
            <div className="kpi-value" style={{ color: passed ? "var(--accent-emerald)" : "var(--accent-crimson)" }}>
              {result.score_10.toFixed(2)} / 10
            </div>
            <div className="kpi-sub">{passed ? "APROBADO (mín. UFV 5.0)" : "SUSPENSO (mín. UFV 5.0)"}</div>
          </div>
          <div className="kpi-card">
            <div className="kpi-label">Preguntas Exactas</div>
            <div className="kpi-value">
              {result.correct_count} / {result.total_questions}
            </div>
            <div className="kpi-sub">Con puntuación parcial en multi-apartado</div>
          </div>
          <div className="kpi-card">
            <div className="kpi-label">Tiempo Empleado</div>
            <div className="kpi-value">{fmtExamClock(result.time_spent_seconds)}</div>
            <div className="kpi-sub">Estado: {result.status}</div>
          </div>
          <div className="kpi-card">
            <div className="kpi-label">Criterio UFV</div>
            <div className="kpi-value" style={{ fontSize: 18 }}>SE1 (50%)</div>
            <div className="kpi-sub">Requiere ≥ 5/10 en teórico-práctico</div>
          </div>
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
          {result.questions.map((q) => (
            <div
              key={q.question_id}
              className="panel"
              style={{
                borderColor: q.is_correct ? "rgba(16, 185, 129, 0.35)" : "rgba(239, 68, 68, 0.35)",
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 10, marginBottom: 10 }}>
                <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  {q.is_correct ? (
                    <CheckCircle2 size={20} style={{ color: "var(--accent-emerald)" }} />
                  ) : (
                    <XCircle size={20} style={{ color: "var(--accent-crimson)" }} />
                  )}
                  <strong>
                    P{q.question_index}. {q.title}
                  </strong>
                  <span className="tag">{q.topic_label}</span>
                </div>
                <span className={`tag ${q.is_correct ? "tag-emerald" : "tag-crimson"}`}>
                  {q.points_earned.toFixed(2)} / {q.points_weight} ptos
                </span>
              </div>

              <div style={{ marginBottom: 12, padding: 12, background: "var(--bg-inset)", borderRadius: 8 }}>
                <MathText content={q.prompt.statement_md} />
              </div>

              <div style={{ marginBottom: 10, fontSize: 13.5 }}>
                <strong>Solución exacta: </strong>
                <MathText content={q.correct_display} />
              </div>

              <ol style={{ margin: "6px 0 0 20px", padding: 0, display: "flex", flexDirection: "column", gap: 6, fontSize: 13.5 }}>
                {q.steps_md.map((st, idx) => (
                  <li key={idx}>
                    <MathText content={st} />
                  </li>
                ))}
              </ol>
            </div>
          ))}
        </div>
      </div>
    );
  }

  // 3. Vista Principal del Simulador y Banco Histórico
  const filteredBank = (bankData?.bank_entries || []).filter(
    (b: any) => bankFilter === "all" || b.topic === bankFilter
  );

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
      {pendingMode && (
        <LockdownRulesModal
          title={pendingMode.title}
          subtitle={`${pendingMode.questions_count} preguntas 100% procedurales únicas · Puntuación oficial sobre 10.`}
          durationLabel={`${pendingMode.duration_minutes} minutos exactos`}
          loading={loading}
          error={modalError}
          onConfirm={handleConfirmStart}
          onCancel={() => setPendingMode(null)}
        />
      )}

      <div className="page-header">
        <div>
          <h1 className="page-title">Simulador de Exámenes y Banco UFV</h1>
          <p className="page-subtitle">
            Basado en las convocatorias CO/CEX 2025–26 y el Banco oficial de 122 preguntas (2022–2026). Cada simulacro genera problemas nuevos.
          </p>
        </div>
      </div>

      <div className="tabs">
        <button type="button" className={`tab-btn ${pageTab === "simulador" ? "active" : ""}`} onClick={() => setPageTab("simulador")}>
          Simulacros Blindados
        </button>
        <button type="button" className={`tab-btn ${pageTab === "banco" ? "active" : ""}`} onClick={() => setPageTab("banco")}>
          Banco Histórico ({bankData?.total_bank_questions || 122} preguntas)
        </button>
        <button type="button" className={`tab-btn ${pageTab === "practicos" ? "active" : ""}`} onClick={() => setPageTab("practicos")}>
          Exámenes Prácticos MATLAB ({bankData?.practical_exams_count || 38})
        </button>
      </div>

      {pageTab === "simulador" && (
        <>
          <div className="grid-3">
            {modes.map((m) => (
              <div key={m.mode} className="panel" style={{ display: "flex", flexDirection: "column", justifyContent: "space-between", gap: 14 }}>
                <div>
                  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 8 }}>
                    <span className="tag tag-blue">{m.duration_minutes} min</span>
                    <span className="tag">{m.questions_count} preguntas</span>
                  </div>
                  <h2 style={{ margin: "0 0 8px", fontSize: 17 }}>{m.title}</h2>
                  <p style={{ margin: 0, fontSize: 13.5, color: "var(--text-secondary)" }}>{m.description}</p>
                </div>
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={() => {
                    setModalError(null);
                    setPendingMode(m);
                  }}
                >
                  <FileCheck2 size={15} /> Iniciar Simulacro Blindado
                </button>
              </div>
            ))}
          </div>

          <div className="panel">
            <h2 className="panel-title">Historial de Simulacros</h2>
            {history.length === 0 ? (
              <p style={{ color: "var(--text-muted)", fontSize: 13.5 }}>
                Aún no has completado ningún simulacro. Elige una modalidad arriba para comenzar.
              </p>
            ) : (
              <div className="table-wrap">
                <table className="data-table">
                  <thead>
                    <tr>
                      <th>Fecha</th>
                      <th>Modalidad</th>
                      <th>Estado</th>
                      <th>Nota /10</th>
                      <th>Aciertos</th>
                      <th>Acción</th>
                    </tr>
                  </thead>
                  <tbody>
                    {history.map((h) => (
                      <tr key={h.exam_id}>
                        <td style={{ fontFamily: "var(--font-mono)", fontSize: 12 }}>
                          {new Date(h.started_at).toLocaleString("es-ES")}
                        </td>
                        <td>{h.title}</td>
                        <td>
                          {h.status === "invalidated" ? (
                            <span className="tag tag-crimson">Invalidado ({h.invalidation_reason})</span>
                          ) : h.status === "timeout" ? (
                            <span className="tag tag-amber">Tiempo agotado</span>
                          ) : (
                            <span className="tag tag-emerald">Completado</span>
                          )}
                        </td>
                        <td style={{ fontFamily: "var(--font-mono)", fontWeight: 700 }}>
                          {h.status === "invalidated" ? "—" : `${h.score_10.toFixed(2)} / 10`}
                        </td>
                        <td style={{ fontFamily: "var(--font-mono)" }}>
                          {h.correct_count}/{h.total_questions}
                        </td>
                        <td>
                          {h.can_review ? (
                            <button
                              type="button"
                              className="btn btn-sm btn-secondary"
                              onClick={() => handleReviewPastExam(h.exam_id)}
                            >
                              Ver corrección
                            </button>
                          ) : (
                            <span style={{ fontSize: 12, color: "var(--text-muted)" }}>Bloqueada</span>
                          )}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </>
      )}

      {pageTab === "banco" && (
        <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 10 }}>
            <div>
              <h2 className="panel-title" style={{ margin: 0 }}>
                Índice Oficial del Banco de Preguntas UFV (2022/23–2025/26)
              </h2>
              <p style={{ margin: "4px 0 0", fontSize: 13, color: "var(--text-secondary)" }}>
                Las respuestas permanecen ocultas para evitar memorización pasiva. Pulsa en cualquier tema para entrenar variantes procedurales únicas.
              </p>
            </div>
            <select
              className="select"
              style={{ width: 260 }}
              value={bankFilter}
              onChange={(e) => setBankFilter(e.target.value)}
            >
              <option value="all">Todos los temas ({bankData?.total_bank_questions || 0})</option>
              <option value="sistemas">Tema 1 · Sistemas</option>
              <option value="matrices">Tema 2 · Matrices</option>
              <option value="espacios_vectoriales">Tema 4 · Espacios Vectoriales</option>
              <option value="aplicaciones_lineales">Tema 5 · Transformaciones Lineales</option>
              <option value="diagonalizacion">Tema 6 · Diagonalización</option>
            </select>
          </div>

          <div className="grid-2">
            {filteredBank.map((q: any) => (
              <div
                key={q.code}
                style={{
                  padding: 14,
                  background: "var(--bg-inset)",
                  border: "1px solid var(--border-subtle)",
                  borderRadius: 8,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "space-between",
                  gap: 10,
                }}
              >
                <div>
                  <div style={{ display: "flex", justifyContent: "space-between", gap: 8, marginBottom: 6 }}>
                    <span className="tag tag-blue">{q.code}</span>
                    <span style={{ fontSize: 11, fontFamily: "var(--font-mono)", color: "var(--text-muted)" }}>
                      {q.exam_origin}
                    </span>
                  </div>
                  <div style={{ fontWeight: 700, fontSize: 14, marginBottom: 6 }}>{q.title}</div>
                  <pre
                    style={{
                      margin: 0,
                      whiteSpace: "pre-wrap",
                      fontFamily: "var(--font-sans)",
                      fontSize: 12.5,
                      color: "var(--text-secondary)",
                      maxHeight: 110,
                      overflow: "hidden",
                    }}
                  >
                    {q.statement_preview}
                  </pre>
                </div>
                <button
                  type="button"
                  className="btn btn-sm btn-secondary"
                  onClick={() => navigate(`/ejercicios?topic=${q.topic}`)}
                >
                  <Cpu size={13} /> Practicar variante procedural en Modo Blindado
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      {pageTab === "practicos" && (
        <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 12 }}>
          <h2 className="panel-title">Enunciados de Exámenes Prácticos MATLAB (CO y CEX 2025/26)</h2>
          <p style={{ margin: 0, fontSize: 13, color: "var(--text-secondary)" }}>
            Siglas oficiales: <code>AR</code> Asignación de Recursos · <code>DC</code> Distribución de Calor · <code>FR</code> Flujo de Redes · <code>GR</code> Grafos · <code>IP</code> Interpolación Polinómica · <code>LEO</code> Leontief · <code>MK</code> Markov · <code>PR</code> PageRank.
          </p>
          <div className="grid-2">
            {(bankData?.practical_variants || []).map((pv: any, i: number) => (
              <div
                key={i}
                style={{
                  padding: 14,
                  background: "var(--bg-inset)",
                  border: "1px solid var(--border-subtle)",
                  borderRadius: 8,
                }}
              >
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
                  <span className="tag tag-amber">{pv.convocatoria}</span>
                  <span style={{ fontSize: 11, fontFamily: "var(--font-mono)", color: "var(--text-muted)" }}>
                    {pv.source}
                  </span>
                </div>
                <div style={{ fontWeight: 700, fontSize: 14, marginBottom: 8 }}>{pv.title}</div>
                <div style={{ maxHeight: 200, overflowY: "auto", fontSize: 13 }}>
                  <MathText content={pv.excerpt_md} />
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
