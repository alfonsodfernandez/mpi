import React, { useEffect, useRef, useState } from "react";
import { Eraser, PenTool, RotateCcw, Trash2, Type } from "lucide-react";

const PEN_COLORS = [
  { name: "Tiza", value: "#f1f5f9" },
  { name: "Cian", value: "#38bdf8" },
  { name: "Ámbar", value: "#fbbf24" },
  { name: "Verde", value: "#34d399" },
];

const MATH_SYMBOLS = ["→", "↔", "λ", "≠", "≤", "≥", "∈", "ℝ", "∞", "½", "⅓", "¼", "±", "·"];

export const Scratchpad: React.FC = () => {
  const [tab, setTab] = useState<"canvas" | "text">("canvas");
  const [color, setColor] = useState("#f1f5f9");
  const [tool, setTool] = useState<"pen" | "eraser">("pen");
  const [lineWidth, setLineWidth] = useState(2.2);
  const [notes, setNotes] = useState("");
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const drawingRef = useRef(false);
  const historyRef = useRef<string[]>([]);

  const initCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const rect = canvas.getBoundingClientRect();
    const w = Math.max(300, Math.floor(rect.width));
    const h = 360;
    if (canvas.width !== w || canvas.height !== h) {
      const prev = canvas.width > 0 ? canvas.toDataURL() : null;
      canvas.width = w;
      canvas.height = h;
      const ctx = canvas.getContext("2d");
      if (ctx) {
        ctx.fillStyle = "#090d14";
        ctx.fillRect(0, 0, w, h);
        if (prev) {
          const img = new Image();
          img.onload = () => ctx.drawImage(img, 0, 0);
          img.src = prev;
        }
      }
    }
  };

  useEffect(() => {
    if (tab === "canvas") {
      initCanvas();
    }
  }, [tab]);

  const saveSnapshot = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    historyRef.current = [...historyRef.current.slice(-15), canvas.toDataURL()];
  };

  const getPos = (e: React.PointerEvent<HTMLCanvasElement>) => {
    const rect = e.currentTarget.getBoundingClientRect();
    return { x: e.clientX - rect.left, y: e.clientY - rect.top };
  };

  const handlePointerDown = (e: React.PointerEvent<HTMLCanvasElement>) => {
    initCanvas();
    saveSnapshot();
    const canvas = canvasRef.current;
    const ctx = canvas?.getContext("2d");
    if (!canvas || !ctx) return;
    e.currentTarget.setPointerCapture(e.pointerId);
    drawingRef.current = true;
    const { x, y } = getPos(e);
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    ctx.strokeStyle = tool === "eraser" ? "#090d14" : color;
    ctx.lineWidth = tool === "eraser" ? 18 : lineWidth;
  };

  const handlePointerMove = (e: React.PointerEvent<HTMLCanvasElement>) => {
    if (!drawingRef.current) return;
    const ctx = canvasRef.current?.getContext("2d");
    if (!ctx) return;
    const { x, y } = getPos(e);
    ctx.lineTo(x, y);
    ctx.stroke();
  };

  const handlePointerUp = () => {
    drawingRef.current = false;
  };

  const handleUndo = () => {
    const canvas = canvasRef.current;
    const ctx = canvas?.getContext("2d");
    const last = historyRef.current.pop();
    if (!canvas || !ctx || !last) return;
    const img = new Image();
    img.onload = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(img, 0, 0);
    };
    img.src = last;
  };

  const handleClear = () => {
    if (tab === "text") {
      setNotes("");
      return;
    }
    const canvas = canvasRef.current;
    const ctx = canvas?.getContext("2d");
    if (!canvas || !ctx) return;
    saveSnapshot();
    ctx.fillStyle = "#090d14";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  };

  return (
    <div className="scratchpad-box">
      <div className="scratchpad-toolbar">
        <div style={{ display: "flex", gap: 6 }}>
          <button
            type="button"
            className={`btn btn-sm ${tab === "canvas" ? "btn-primary" : "btn-secondary"}`}
            onClick={() => setTab("canvas")}
          >
            <PenTool size={13} /> Pizarra
          </button>
          <button
            type="button"
            className={`btn btn-sm ${tab === "text" ? "btn-primary" : "btn-secondary"}`}
            onClick={() => setTab("text")}
          >
            <Type size={13} /> Bloc rápido
          </button>
        </div>

        <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
          {tab === "canvas" && (
            <>
              {PEN_COLORS.map((c) => (
                <button
                  key={c.value}
                  type="button"
                  title={c.name}
                  onClick={() => {
                    setTool("pen");
                    setColor(c.value);
                  }}
                  style={{
                    width: 18,
                    height: 18,
                    borderRadius: "50%",
                    background: c.value,
                    border: tool === "pen" && color === c.value ? "2px solid #fff" : "1px solid #334155",
                    cursor: "pointer",
                  }}
                />
              ))}
              <button
                type="button"
                className={`btn btn-sm ${tool === "eraser" ? "btn-danger" : "btn-ghost"}`}
                onClick={() => setTool(tool === "eraser" ? "pen" : "eraser")}
                title="Borrador"
              >
                <Eraser size={13} />
              </button>
              <select
                className="select"
                value={lineWidth}
                onChange={(e) => setLineWidth(Number(e.target.value))}
                style={{ width: 62, padding: "4px 6px", fontSize: 12 }}
                aria-label="Grosor del trazo"
              >
                <option value={1.5}>Fino</option>
                <option value={2.2}>Med</option>
                <option value={4}>Grueso</option>
              </select>
              <button type="button" className="btn btn-sm btn-ghost" onClick={handleUndo} title="Deshacer">
                <RotateCcw size={13} />
              </button>
            </>
          )}
          <button type="button" className="btn btn-sm btn-ghost" onClick={handleClear} title="Limpiar">
            <Trash2 size={13} />
          </button>
        </div>
      </div>

      {tab === "canvas" ? (
        <canvas
          ref={canvasRef}
          className="scratchpad-canvas"
          onPointerDown={handlePointerDown}
          onPointerMove={handlePointerMove}
          onPointerUp={handlePointerUp}
          onPointerCancel={handlePointerUp}
        />
      ) : (
        <div style={{ padding: 12, display: "flex", flexDirection: "column", gap: 8 }}>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 4 }}>
            {MATH_SYMBOLS.map((sym) => (
              <button
                key={sym}
                type="button"
                className="btn btn-sm btn-secondary"
                style={{ padding: "3px 8px", fontFamily: "var(--font-mono)" }}
                onClick={() => setNotes((n) => n + sym)}
              >
                {sym}
              </button>
            ))}
          </div>
          <textarea
            className="textarea input-mono"
            rows={13}
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            placeholder={"Escribe aquí tus pasos en sucio (ej. F2 <- F2 - 2*F1)...\nNo salgas de la ventana para hacer cuentas."}
          />
        </div>
      )}
    </div>
  );
};
