import React, { useCallback, useEffect, useRef } from "react";
import { AlertTriangle, Maximize2, ShieldAlert, ShieldCheck, Timer } from "lucide-react";
import { apiFetch } from "../api/client";

/** Sintetiza una alerta sonora clara vía Web Audio API sin depender de ficheros externos. */
export function playAlertBeep(urgent: boolean = true): void {
  try {
    const AudioCtx = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
    if (!AudioCtx) return;
    const ctx = new AudioCtx();
    const now = ctx.currentTime;
    const freqs = urgent ? [880, 620, 880] : [520];
    freqs.forEach((f, i) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = urgent ? "sawtooth" : "triangle";
      osc.frequency.setValueAtTime(f, now + i * 0.14);
      gain.gain.setValueAtTime(0.08, now + i * 0.14);
      gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.14 + 0.12);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now + i * 0.14);
      osc.stop(now + i * 0.14 + 0.13);
    });
  } catch {
    // ignore autoplay restriction
  }
}

export async function enterFullscreenSafely(): Promise<boolean> {
  try {
    if (document.fullscreenElement) return true;
    const el = document.documentElement;
    if (el.requestFullscreen) {
      await el.requestFullscreen();
      return Boolean(document.fullscreenElement);
    }
    return false;
  } catch {
    return false;
  }
}

export async function exitFullscreenSafely(): Promise<void> {
  try {
    if (document.fullscreenElement && document.exitFullscreen) {
      await document.exitFullscreen();
    }
  } catch {
    // ignore
  }
}

export interface BreachInfo {
  violationType: string;
  label: string;
  details: string;
  timestamp: string;
}

const VIOLATION_LABELS: Record<string, string> = {
  EXIT_FULLSCREEN: "Salida de Pantalla Completa",
  TAB_SWITCH: "Cambio de Pestaña del Navegador",
  WINDOW_BLUR: "Pérdida de Foco de Ventana (Alt+Tab / otra app)",
  DEVTOOLS_ATTEMPT: "Intento de Abrir Herramientas de Desarrollador (F12 / Inspector)",
  COPY_ATTEMPT: "Intento de Copiar / Pegar Contenido Protegido",
  CONTEXT_MENU: "Intento de Menú Contextual (Clic Derecho)",
  SCREENSHOT_ATTEMPT: "Tecla de Captura de Pantalla Detectada",
};

interface UseLockdownOptions {
  active: boolean;
  contextMode: "practice" | "exam" | "matlab";
  topic: string;
  questionRef: string;
  activeAttemptId?: string | null;
  activeExamId?: string | null;
  onMajorBreach: (breach: BreachInfo) => void;
  onMinorWarning: (msg: string) => void;
}

export function useLockdownGuardian({
  active,
  contextMode,
  topic,
  questionRef,
  activeAttemptId,
  activeExamId,
  onMajorBreach,
  onMinorWarning,
}: UseLockdownOptions) {
  const breachLockRef = useRef(false);
  const copyCountRef = useRef(0);
  // Grace period de 1000ms justo al entrar en fullscreen para evitar falsos positivos del SO
  const armedAtRef = useRef<number>(0);

  const onMajorRef = useRef(onMajorBreach);
  const onMinorRef = useRef(onMinorWarning);
  const metaRef = useRef({ contextMode, topic, questionRef, activeAttemptId, activeExamId });

  useEffect(() => {
    onMajorRef.current = onMajorBreach;
    onMinorRef.current = onMinorWarning;
    metaRef.current = { contextMode, topic, questionRef, activeAttemptId, activeExamId };
  }, [onMajorBreach, onMinorWarning, contextMode, topic, questionRef, activeAttemptId, activeExamId]);

  useEffect(() => {
    if (active) {
      breachLockRef.current = false;
      copyCountRef.current = 0;
      armedAtRef.current = Date.now() + 1000;
    }
  }, [active, activeAttemptId, activeExamId]);

  const reportToServer = useCallback(
    async (
      violationType: string,
      severity: "high" | "medium",
      details: string,
      triggerReset: boolean
    ) => {
      const m = metaRef.current;
      try {
        await apiFetch("/api/security/violation", {
          method: "POST",
          body: JSON.stringify({
            violation_type: violationType,
            severity,
            context_mode: m.contextMode,
            topic: m.topic,
            question_ref: m.questionRef,
            details,
            active_attempt_id: m.activeAttemptId || null,
            active_exam_id: m.activeExamId || null,
            trigger_reset: triggerReset,
          }),
        });
      } catch {
        // Incluso si falla la red, bloqueamos localmente
      }
    },
    []
  );

  const triggerMajor = useCallback(
    (violationType: string, details: string) => {
      if (!active || breachLockRef.current) return;
      breachLockRef.current = true;
      playAlertBeep(true);
      void reportToServer(violationType, "high", details, true);
      onMajorRef.current({
        violationType,
        label: VIOLATION_LABELS[violationType] || violationType,
        details,
        timestamp: new Date().toLocaleTimeString("es-ES"),
      });
    },
    [active, reportToServer]
  );

  const triggerMinor = useCallback(
    (violationType: string, details: string) => {
      if (!active || breachLockRef.current) return;
      copyCountRef.current += 1;
      playAlertBeep(false);
      if (copyCountRef.current >= 3) {
        triggerMajor(violationType, `${details} (3 intentos reiterados: reinicio forzado)`);
        return;
      }
      void reportToServer(violationType, "medium", details, false);
      onMinorRef.current(
        `Acción bloqueada (${VIOLATION_LABELS[violationType] || violationType}). Registrado en auditoría (${copyCountRef.current}/3 antes de reinicio automático).`
      );
    },
    [active, reportToServer, triggerMajor]
  );

  useEffect(() => {
    if (!active) return;

    const onFullscreenChange = () => {
      if (Date.now() < armedAtRef.current) return;
      if (!document.fullscreenElement) {
        triggerMajor("EXIT_FULLSCREEN", "El navegador salió del modo pantalla completa obligatoria.");
      }
    };

    const onVisibilityChange = () => {
      if (Date.now() < armedAtRef.current) return;
      if (document.hidden) {
        triggerMajor("TAB_SWITCH", "Se detectó cambio de pestaña o minimización del navegador.");
      }
    };

    const onWindowBlur = () => {
      if (Date.now() < armedAtRef.current) return;
      triggerMajor("WINDOW_BLUR", "La ventana perdió el foco (Alt+Tab o cambio a otra aplicación).");
    };

    const onKeyDown = (e: KeyboardEvent) => {
      const key = e.key.toLowerCase();
      const ctrl = e.ctrlKey || e.metaKey;

      // Bloquear DevTools
      if (
        e.key === "F12" ||
        (ctrl && e.shiftKey && ["i", "j", "c"].includes(key)) ||
        (ctrl && key === "u")
      ) {
        e.preventDefault();
        e.stopPropagation();
        triggerMajor("DEVTOOLS_ATTEMPT", `Atajo de inspección bloqueado (${e.key}).`);
        return;
      }

      // Captura de pantalla
      if (e.key === "PrintScreen") {
        e.preventDefault();
        triggerMajor("SCREENSHOT_ATTEMPT", "Pulsación de PrintScreen detectada.");
        return;
      }

      // Bloquear portapapeles
      if (ctrl && ["c", "v", "x", "a"].includes(key)) {
        const target = e.target as HTMLElement | null;
        const isEditable = target && (target.tagName === "INPUT" || target.tagName === "TEXTAREA");
        if (!isEditable || ["c", "v", "x"].includes(key)) {
          e.preventDefault();
          e.stopPropagation();
          triggerMinor("COPY_ATTEMPT", `Atajo de portapapeles bloqueado (Ctrl+${key.toUpperCase()}).`);
        }
      }
    };

    const onContextMenu = (e: MouseEvent) => {
      e.preventDefault();
      triggerMinor("CONTEXT_MENU", "Clic derecho bloqueado en Modo Estudio Blindado.");
    };

    const onPaste = (e: ClipboardEvent) => {
      e.preventDefault();
      triggerMinor("COPY_ATTEMPT", "Pegado desde portapapeles bloqueado en Modo Blindado.");
    };

    // Captura el desfase base al entrar en fullscreen para evitar falsos positivos por zoom del navegador
    let baseWidthGap: number | null = null;
    let baseHeightGap: number | null = null;

    // Watchdog redundante cada 500ms: verifica fullscreen, visibilidad y apertura de DevTools acoplado
    const watchdog = window.setInterval(() => {
      if (Date.now() < armedAtRef.current) return;
      if (!document.fullscreenElement) {
        triggerMajor("EXIT_FULLSCREEN", "Se detectó pérdida del modo pantalla completa obligatoria.");
        return;
      }
      if (document.hidden) {
        triggerMajor("TAB_SWITCH", "Pestaña oculta detectada durante Modo Blindado.");
        return;
      }
      const widthGap = window.outerWidth - window.innerWidth;
      const heightGap = window.outerHeight - window.innerHeight;
      if (baseWidthGap === null || baseHeightGap === null) {
        baseWidthGap = widthGap;
        baseHeightGap = heightGap;
        return;
      }
      if (widthGap - baseWidthGap > 200 || heightGap - baseHeightGap > 200) {
        triggerMajor("DEVTOOLS_ATTEMPT", "Reducción súbita del viewport compatible con apertura de DevTools.");
      }
    }, 500);

    document.addEventListener("fullscreenchange", onFullscreenChange);
    document.addEventListener("visibilitychange", onVisibilityChange);
    window.addEventListener("blur", onWindowBlur);
    window.addEventListener("keydown", onKeyDown, true);
    document.addEventListener("contextmenu", onContextMenu, true);
    document.addEventListener("paste", onPaste, true);

    return () => {
      window.clearInterval(watchdog);
      document.removeEventListener("fullscreenchange", onFullscreenChange);
      document.removeEventListener("visibilitychange", onVisibilityChange);
      window.removeEventListener("blur", onWindowBlur);
      window.removeEventListener("keydown", onKeyDown, true);
      document.removeEventListener("contextmenu", onContextMenu, true);
      document.removeEventListener("paste", onPaste, true);
    };
  }, [active, triggerMajor, triggerMinor]);

  return { triggerMinor };
}

export const LockdownRulesModal: React.FC<{
  title: string;
  subtitle: string;
  durationLabel: string;
  loading?: boolean;
  error?: string | null;
  onConfirm: () => void;
  onCancel: () => void;
}> = ({ title, subtitle, durationLabel, loading, error, onConfirm, onCancel }) => {
  return (
    <div className="modal-backdrop" role="dialog" aria-modal="true">
      <div className="modal-card">
        <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 14 }}>
          <div
            style={{
              width: 42,
              height: 42,
              borderRadius: 10,
              background: "rgba(245, 158, 11, 0.14)",
              border: "1px solid rgba(245, 158, 11, 0.35)",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              color: "#fbbf24",
              flexShrink: 0,
            }}
          >
            <ShieldCheck size={22} />
          </div>
          <div>
            <h2 style={{ margin: 0, fontSize: 19, letterSpacing: "-0.02em" }}>{title}</h2>
            <div style={{ fontSize: 13, color: "var(--text-secondary)", marginTop: 2 }}>{subtitle}</div>
          </div>
        </div>

        <div
          style={{
            background: "var(--bg-inset)",
            border: "1px solid var(--border-subtle)",
            borderRadius: 10,
            padding: "14px 16px",
            marginBottom: 18,
            display: "flex",
            flexDirection: "column",
            gap: 10,
            fontSize: 13.5,
          }}
        >
          <div style={{ fontWeight: 600, color: "var(--accent-amber)", fontSize: 12.5, fontFamily: "var(--font-mono)" }}>
            NORMAS DEL MODO ESTUDIO BLINDADO (LOCKDOWN)
          </div>
          <div style={{ display: "flex", gap: 10, alignItems: "flex-start" }}>
            <Maximize2 size={16} style={{ color: "var(--accent-cyan)", marginTop: 3, flexShrink: 0 }} />
            <span>
              <strong>Pantalla completa obligatoria:</strong> la sesión solo arranca al aceptar pantalla completa.
            </span>
          </div>
          <div style={{ display: "flex", gap: 10, alignItems: "flex-start" }}>
            <ShieldAlert size={16} style={{ color: "var(--accent-crimson)", marginTop: 3, flexShrink: 0 }} />
            <span>
              <strong>Prohibido cambiar de ventana o pestaña:</strong> si sales de pantalla completa, cambias de pestaña, usas Alt+Tab o abres F12/Inspector, la sesión se bloqueará con alerta, <strong>quedará registrada para el profesor</strong> y se reiniciará desde cero con problemas totalmente nuevos.
            </span>
          </div>
          <div style={{ display: "flex", gap: 10, alignItems: "flex-start" }}>
            <AlertTriangle size={16} style={{ color: "var(--accent-amber)", marginTop: 3, flexShrink: 0 }} />
            <span>
              <strong>Sin copiar ni pegar:</strong> la selección de texto, clic derecho y Ctrl+C/V están desactivados. Dispones de una <strong>Pizarra Digital integrada</strong> en pantalla para tus cálculos en sucio.
            </span>
          </div>
          <div style={{ display: "flex", gap: 10, alignItems: "flex-start" }}>
            <Timer size={16} style={{ color: "var(--accent-emerald)", marginTop: 3, flexShrink: 0 }} />
            <span>
              <strong>Temporizador estricto ({durationLabel}):</strong> al llegar a <code>00:00</code> el intento se envía automáticamente como incompleto. Las soluciones solo se revelan al terminar.
            </span>
          </div>
        </div>

        {error && (
          <div
            style={{
              marginBottom: 14,
              padding: "10px 12px",
              borderRadius: 8,
              background: "rgba(239, 68, 68, 0.14)",
              border: "1px solid rgba(239, 68, 68, 0.35)",
              color: "#fca5a5",
              fontSize: 13,
            }}
          >
            {error}
          </div>
        )}

        <div style={{ display: "flex", justifyContent: "flex-end", gap: 10 }}>
          <button type="button" className="btn btn-secondary" onClick={onCancel} disabled={loading}>
            Cancelar
          </button>
          <button type="button" className="btn btn-primary" onClick={onConfirm} disabled={loading}>
            <Maximize2 size={15} />
            {loading ? "Generando problemas únicos..." : "Entiendo las reglas, comenzar sesión"}
          </button>
        </div>
      </div>
    </div>
  );
};

export const LockdownBreachOverlay: React.FC<{
  breach: BreachInfo;
  onRestart: () => void;
  onExit: () => void;
  restarting?: boolean;
}> = ({ breach, onRestart, onExit, restarting }) => {
  return (
    <div className="breach-overlay" role="alertdialog" aria-modal="true">
      <div className="breach-card">
        <div
          style={{
            width: 58,
            height: 58,
            borderRadius: "50%",
            background: "rgba(239, 68, 68, 0.18)",
            border: "1px solid rgba(239, 68, 68, 0.55)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            color: "#f87171",
            margin: "0 auto 16px",
          }}
        >
          <ShieldAlert size={30} />
        </div>
        <div style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "#f87171", letterSpacing: "0.08em" }}>
          BLOQUEO DE SEGURIDAD · INFRACCIÓN REGISTRADA ({breach.timestamp})
        </div>
        <h2 style={{ margin: "8px 0 10px", fontSize: 22, color: "#fff" }}>{breach.label}</h2>
        <p style={{ margin: "0 0 18px", fontSize: 14, color: "#fecaca" }}>{breach.details}</p>

        <div
          style={{
            background: "rgba(0,0,0,0.35)",
            border: "1px solid rgba(239,68,68,0.28)",
            borderRadius: 8,
            padding: "12px 14px",
            marginBottom: 22,
            fontSize: 13,
            color: "#fca5a5",
            textAlign: "left",
          }}
        >
          • Este evento ha sido registrado en la base de datos de auditoría del profesor.<br />
          • El ejercicio/examen en curso ha sido <strong>invalidado en el servidor</strong>.<br />
          • Al reiniciar, el motor matemático generará <strong>problemas completamente nuevos</strong>.
        </div>

        <div style={{ display: "flex", gap: 10, justifyContent: "center", flexWrap: "wrap" }}>
          <button type="button" className="btn btn-secondary" onClick={onExit} disabled={restarting}>
            Salir al menú
          </button>
          <button type="button" className="btn btn-primary" onClick={onRestart} disabled={restarting}>
            <Maximize2 size={15} />
            {restarting ? "Generando nuevos problemas..." : "Reingresar en Pantalla Completa y Reiniciar"}
          </button>
        </div>
      </div>
    </div>
  );
};
