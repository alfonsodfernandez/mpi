import React, { useCallback, useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import {
  ArrowRight,
  CheckCircle2,
  Cpu,
  LogOut,
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
import { ExerciseFeedback, PublicExercise, UserInfo } from "../types";

interface CatalogTopic {
  topic: string;
  label: string;
  generators: { id: string; label: string; difficulty: string; topic: string }[];
}

function fmtClock(sec: number): string {
  const s = Math.max(0, sec);
  const m = Math.floor(s / 60);
  const rem = s % 60;
  return `${String(m).padStart(2, "0")}:${String(rem).padStart(2, "0")}`;
}

export const PracticePage: React.FC<{ user: UserInfo }> = ({ user }) => {
  const [searchParams] = useSearchParams();
  const [catalog, setCatalog] = useState<CatalogTopic[]>([]);
  const [selectedTopic, setSelectedTopic] = useState<string>(searchParams.get("topic") || "random");
  const [selectedGen, setSelectedGen] = useState<string>("");
  const [history, setHistory] = useState<any[]>([]);

  // Estado Lockdown y ejercicio activo
  const [showRulesModal, setShowRulesModal] = useState(false);
  const [modalError, setModalError] = useState<string | null>(null);
  const [loadingStart, setLoadingStart] = useState(false);

  const [exercise, setExercise] = useState<PublicExercise | null>(null);
  const [answer, setAnswer] = useState<any>("");
  const [feedback, setFeedback] = useState<ExerciseFeedback | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [secondsLeft, setSecondsLeft] = useState<number>(0);

  const [breach, setBreach] = useState<BreachInfo | null>(null);
  const [minorToast, setMinorToast] = useState<string | null>(null);

  const loadMeta = useCallback(() => {
    apiFetch<{ topics: CatalogTopic[] }>("/api/exercises/catalog").then((r) => setCatalog(r.topics));
    apiFetch<{ attempts: any[] }>("/api/exercises/history?limit=15").then((r) => setHistory(r.attempts));
  }, []);

  useEffect(() => {
    loadMeta();
  }, [loadMeta]);

  const fetchFreshExercise = useCallback(async () => {
    const body: Record<string, any> = { topic: selectedTopic };
    if (selectedGen) body.generator_id = selectedGen;
    const ex = await apiFetch<PublicExercise>("/api/exercises/start", {
      method: "POST",
      body: JSON.stringify(body),
    });
    setExercise(ex);
    setAnswer(createInitialAnswer(ex.prompt.input_spec));
    setFeedback(null);
    setSecondsLeft(ex.time_limit_seconds);
  }, [selectedTopic, selectedGen]);

  const handleConfirmRulesAndStart = async () => {
    setModalError(null);
    setLoadingStart(true);
    const fsOk = await enterFullscreenSafely();
    if (!fsOk) {
      setModalError(
        "El navegador no permitió entrar en pantalla completa. Haz clic directamente en el botón y permite pantalla completa para iniciar."
      );
      setLoadingStart(false);
      return;
    }
    try {
      await fetchFreshExercise();
      setShowRulesModal(false);
    } catch (err: any) {
      setModalError(err?.message || "No se pudo generar el ejercicio.");
      await exitFullscreenSafely();
    } finally {
      setLoadingStart(false);
    }
  };

  const handleSubmit = useCallback(
    async (timedOut: boolean = false) => {
      if (!exercise || feedback || submitting) return;
      setSubmitting(true);
      try {
        const res = await apiFetch<ExerciseFeedback>(`/api/exercises/${exercise.attempt_id}/submit`, {
          method: "POST",
          body: JSON.stringify({ answer, timed_out: timedOut }),
        });
        setFeedback(res);
        loadMeta();
      } catch (err: any) {
        setMinorToast(err?.message || "Error al corregir la respuesta.");
      } finally {
        setSubmitting(false);
      }
    },
    [exercise, feedback, submitting, answer, loadMeta]
  );

  // Cuenta atrás estricta con auto-envío a 00:00
  useEffect(() => {
    if (!exercise || feedback || breach) return;
    const timer = window.setInterval(() => {
      setSecondsLeft((prev) => {
        if (prev <= 1) {
          window.clearInterval(timer);
          void handleSubmit(true);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => window.clearInterval(timer);
  }, [exercise, feedback, breach, handleSubmit]);

  // Guardián anti-trampas activo SOLO mientras hay ejercicio sin corregir
  const lockdownActive = Boolean(exercise && !feedback && !breach);
  const { triggerMinor } = useLockdownGuardian({
    active: lockdownActive,
    contextMode: selectedTopic === "matlab" ? "matlab" : "practice",
    topic: exercise?.topic || selectedTopic,
    questionRef: exercise?.title || "Ejercicio procedural",
    activeAttemptId: exercise?.attempt_id,
    onMajorBreach: (info) => {
      setBreach(info);
      setExercise(null);
      loadMeta();
    },
    onMinorWarning: (msg) => {
      setMinorToast(msg);
      window.setTimeout(() => setMinorToast(null), 4500);
    },
  });

  const handleRestartAfterBreach = async () => {
    setLoadingStart(true);
    const fsOk = await enterFullscreenSafely();
    if (!fsOk) {
      setLoadingStart(false);
      return;
    }
    try {
      setBreach(null);
      await fetchFreshExercise();
    } finally {
      setLoadingStart(false);
    }
  };

  const handleExitSession = async () => {
    setBreach(null);
    setExercise(null);
    setFeedback(null);
    await exitFullscreenSafely();
    loadMeta();
  };

  const handleNextExercise = async () => {
    // Asegurar que seguimos en pantalla completa antes de lanzar el siguiente ejercicio
    if (!document.fullscreenElement) {
      const ok = await enterFullscreenSafely();
      if (!ok) {
        setShowRulesModal(true);
        setExercise(null);
        return;
      }
    }
    setLoadingStart(true);
    try {
      await fetchFreshExercise();
    } finally {
      setLoadingStart(false);
    }
  };

  const activeTopicCatalog = catalog.find((c) => c.topic === selectedTopic);

  // Vista activa de Entrenamiento en Pantalla Completa (Lockdown Mode)
  if (exercise || breach) {
    const pctLeft = exercise ? secondsLeft / Math.max(1, exercise.time_limit_seconds) : 1;
    const timerClass = pctLeft <= 0.1 ? "critical" : pctLeft <= 0.25 ? "warn" : "";

    return (
      <div style={{ minHeight: "100vh", background: "var(--bg-canvas)" }}>
        {breach && (
          <LockdownBreachOverlay
            breach={breach}
            onRestart={handleRestartAfterBreach}
            onExit={handleExitSession}
            restarting={loadingStart}
          />
        )}

        {minorToast && <div className="toast-alert">{minorToast}</div>}

        {exercise && (
          <>
            <div className="lockdown-bar">
              <div style={{ display: "flex", alignItems: "center", gap: 12, flexWrap: "wrap" }}>
                <span className="tag tag-amber">
                  <Shield size={12} /> MODO BLINDADO ACTIVO
                </span>
                <span className="tag tag-blue">{exercise.topic_label}</span>
                <span style={{ fontWeight: 600, fontSize: 14 }}>{exercise.title}</span>
              </div>

              <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
                  <Timer size={16} style={{ color: "var(--text-muted)" }} />
                  <div className={`lockdown-timer ${timerClass}`}>{fmtClock(secondsLeft)}</div>
                </div>
                {feedback && (
                  <button type="button" className="btn btn-secondary btn-sm" onClick={handleExitSession}>
                    <LogOut size={14} /> Salir del Modo Blindado
                  </button>
                )}
              </div>
            </div>

            <div style={{ maxWidth: 1420, margin: "0 auto", padding: "22px 26px 44px" }}>
              <div className="split-workspace">
                {/* Columna izquierda: Enunciado Blindado + Respuesta + Corrección */}
                <div style={{ display: "flex", flexDirection: "column", gap: 18 }}>
                  <ProtectedPrompt
                    prompt={exercise.prompt}
                    studentName={user.display_name}
                    watermarkBase={exercise.watermark_text}
                    onBlockedAction={(t, d) => triggerMinor(t, d)}
                  />

                  <div className="panel">
                    <h3 className="panel-title">Tu Respuesta</h3>
                    <AnswerInput
                      spec={exercise.prompt.input_spec}
                      value={answer}
                      onChange={setAnswer}
                      disabled={Boolean(feedback) || submitting}
                    />

                    {!feedback && (
                      <div style={{ marginTop: 18, display: "flex", justifyContent: "space-between", alignItems: "center", gap: 12, flexWrap: "wrap" }}>
                        <span style={{ fontSize: 12, color: "var(--text-muted)" }}>
                          La solución exacta y los pasos se desbloquearán en el servidor al enviar.
                        </span>
                        <button
                          type="button"
                          className="btn btn-primary"
                          onClick={() => handleSubmit(false)}
                          disabled={submitting}
                        >
                          <Send size={15} /> {submitting ? "Corrigiendo con SymPy..." : "Comprobar Respuesta"}
                        </button>
                      </div>
                    )}
                  </div>

                  {/* Solución revelada SOLO tras submit o timeout */}
                  {feedback && (
                    <div
                      className="panel"
                      style={{
                        borderColor: feedback.is_correct ? "rgba(16, 185, 129, 0.5)" : "rgba(239, 68, 68, 0.45)",
                        background: feedback.is_correct ? "rgba(16, 185, 129, 0.06)" : "rgba(239, 68, 68, 0.06)",
                      }}
                    >
                      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 12, marginBottom: 14 }}>
                        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                          {feedback.is_correct ? (
                            <CheckCircle2 size={24} style={{ color: "var(--accent-emerald)" }} />
                          ) : (
                            <XCircle size={24} style={{ color: "var(--accent-crimson)" }} />
                          )}
                          <div>
                            <div style={{ fontSize: 17, fontWeight: 700 }}>
                              {feedback.is_correct
                                ? "¡Respuesta Correcta!"
                                : feedback.status === "timeout"
                                ? "Tiempo Agotado"
                                : "Respuesta Incorrecta"}
                            </div>
                            <div style={{ fontSize: 13, color: "var(--text-secondary)" }}>
                              <MathText content={feedback.feedback} />
                            </div>
                          </div>
                        </div>

                        <div style={{ display: "flex", gap: 8 }}>
                          <span className="tag">Tiempo: {feedback.time_spent_seconds}s</span>
                          <span className={`tag ${feedback.is_correct ? "tag-emerald" : "tag-crimson"}`}>
                            Puntuación: {Math.round(feedback.score * 100)}%
                          </span>
                        </div>
                      </div>

                      <div
                        style={{
                          padding: "12px 14px",
                          background: "var(--bg-inset)",
                          borderRadius: 8,
                          border: "1px solid var(--border-subtle)",
                          marginBottom: 14,
                        }}
                      >
                        <div style={{ fontSize: 11.5, fontFamily: "var(--font-mono)", color: "var(--accent-cyan)", marginBottom: 4 }}>
                          SOLUCIÓN EXACTA VERIFICADA POR SYMPY
                        </div>
                        <MathText content={feedback.correct_display} />
                      </div>

                      <div style={{ marginBottom: 16 }}>
                        <div style={{ fontSize: 13, fontWeight: 700, marginBottom: 8 }}>Resolución paso a paso:</div>
                        <ol style={{ margin: "0 0 0 20px", padding: 0, display: "flex", flexDirection: "column", gap: 8 }}>
                          {feedback.steps_md.map((st, idx) => (
                            <li key={idx}>
                              <MathText content={st} />
                            </li>
                          ))}
                        </ol>
                        <div style={{ marginTop: 10, fontSize: 12, color: "var(--text-muted)", fontFamily: "var(--font-mono)" }}>
                          Referencia: {feedback.theory_ref}
                        </div>
                      </div>

                      <div style={{ display: "flex", gap: 10, justifyContent: "flex-end" }}>
                        <button type="button" className="btn btn-secondary" onClick={handleExitSession}>
                          Terminar bloque
                        </button>
                        <button type="button" className="btn btn-primary" onClick={handleNextExercise} disabled={loadingStart}>
                          {loadingStart ? "Generando..." : "Siguiente Ejercicio Único"} <ArrowRight size={15} />
                        </button>
                      </div>
                    </div>
                  )}
                </div>

                {/* Columna derecha: Pizarra Digital + Bloc de Cálculos en sucio */}
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

  // Selector de configuración antes de entrar en Modo Blindado
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 22 }}>
      {showRulesModal && (
        <LockdownRulesModal
          title="Entrenamiento Infinito en Modo Blindado"
          subtitle="Cada problema es generado algorítmicamente en el servidor. Nunca repetirás el mismo ejercicio."
          durationLabel="2.5 a 6 min según dificultad"
          loading={loadingStart}
          error={modalError}
          onConfirm={handleConfirmRulesAndStart}
          onCancel={() => setShowRulesModal(false)}
        />
      )}

      <div className="page-header">
        <div>
          <h1 className="page-title">Motor de Ejercicios Infinitos</h1>
          <p className="page-subtitle">
            26 generadores procedurales exactos con SymPy · Sin repeticiones · Modo pantalla completa blindado con Pizarra Digital.
          </p>
        </div>
      </div>

      <div className="grid-2">
        <div className="panel" style={{ display: "flex", flexDirection: "column", gap: 16 }}>
          <h2 className="panel-title">
            <Cpu size={17} style={{ color: "var(--accent-cyan)" }} /> Configurar Sesión de Entrenamiento
          </h2>

          <div>
            <label style={{ display: "block", fontSize: 13, fontWeight: 600, color: "var(--text-secondary)", marginBottom: 8 }}>
              1. Elige el bloque temático
            </label>
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(190px, 1fr))", gap: 8 }}>
              <button
                type="button"
                className={`choice-option ${selectedTopic === "random" ? "selected" : ""}`}
                onClick={() => {
                  setSelectedTopic("random");
                  setSelectedGen("");
                }}
              >
                <div>
                  <div style={{ fontWeight: 600 }}>Todos los temas (Mix)</div>
                  <div style={{ fontSize: 12, color: "var(--text-muted)" }}>26 tipos procedurales</div>
                </div>
              </button>
              {catalog.map((c) => (
                <button
                  key={c.topic}
                  type="button"
                  className={`choice-option ${selectedTopic === c.topic ? "selected" : ""}`}
                  onClick={() => {
                    setSelectedTopic(c.topic);
                    setSelectedGen("");
                  }}
                >
                  <div>
                    <div style={{ fontWeight: 600 }}>{c.label}</div>
                    <div style={{ fontSize: 12, color: "var(--text-muted)" }}>{c.generators.length} generadores</div>
                  </div>
                </button>
              ))}
            </div>
          </div>

          {activeTopicCatalog && (
            <div>
              <label style={{ display: "block", fontSize: 13, fontWeight: 600, color: "var(--text-secondary)", marginBottom: 6 }}>
                2. Tipo de ejercicio concreto (opcional)
              </label>
              <select
                className="select"
                value={selectedGen}
                onChange={(e) => setSelectedGen(e.target.value)}
              >
                <option value="">Aleatorio dentro de {activeTopicCatalog.label}</option>
                {activeTopicCatalog.generators.map((g) => (
                  <option key={g.id} value={g.id}>
                    {g.label} (Dificultad: {g.difficulty})
                  </option>
                ))}
              </select>
            </div>
          )}

          <button
            type="button"
            className="btn btn-primary"
            style={{ padding: "12px 18px", fontSize: 14.5 }}
            onClick={() => {
              setModalError(null);
              setShowRulesModal(true);
            }}
          >
            <Shield size={16} /> Comenzar Entrenamiento en Modo Blindado
          </button>
        </div>

        <div className="panel">
          <h2 className="panel-title">Historial Reciente</h2>
          {history.length === 0 ? (
            <p style={{ color: "var(--text-muted)", fontSize: 13.5 }}>
              Todavía no has completado ejercicios en esta cuenta. ¡Empieza tu primera sesión blindada!
            </p>
          ) : (
            <div className="table-wrap">
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Ejercicio</th>
                    <th>Estado</th>
                    <th>Tiempo</th>
                  </tr>
                </thead>
                <tbody>
                  {history.map((h) => (
                    <tr key={h.attempt_id}>
                      <td>
                        <div style={{ fontWeight: 600, fontSize: 13 }}>{h.title}</div>
                        <div style={{ fontSize: 11.5, color: "var(--text-muted)" }}>{h.topic_label}</div>
                      </td>
                      <td>
                        {h.status === "invalidated" ? (
                          <span className="tag tag-crimson">Invalidado</span>
                        ) : h.status === "timeout" ? (
                          <span className="tag tag-amber">Timeout</span>
                        ) : h.is_correct ? (
                          <span className="tag tag-emerald">Correcto</span>
                        ) : (
                          <span className="tag tag-crimson">Incorrecto ({Math.round(h.score * 100)}%)</span>
                        )}
                      </td>
                      <td style={{ fontFamily: "var(--font-mono)", fontSize: 12 }}>
                        {h.time_spent_seconds ? `${h.time_spent_seconds}s` : "—"}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
