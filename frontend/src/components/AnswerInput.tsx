import React from "react";
import { InputSpec } from "../types";
import { MathText } from "./MathText";

interface AnswerInputProps {
  spec: InputSpec;
  value: any;
  onChange: (val: any) => void;
  disabled?: boolean;
}

export function createInitialAnswer(spec: InputSpec): any {
  switch (spec.kind) {
    case "number":
      return "";
    case "vector":
      return (spec.labels || []).map(() => "");
    case "matrix":
      return Array.from({ length: spec.rows || 2 }, () =>
        Array.from({ length: spec.cols || 2 }, () => "")
      );
    case "choice":
      return "";
    case "multi_tf": {
      const obj: Record<string, boolean | null> = {};
      (spec.items || []).forEach((it) => {
        obj[it.id] = null;
      });
      return obj;
    }
    case "multi_field": {
      const obj: Record<string, any> = {};
      (spec.fields || []).forEach((f) => {
        obj[f.id] = f.type === "vector" ? (f.labels || []).map(() => "") : "";
      });
      return obj;
    }
    default:
      return "";
  }
}

export const AnswerInput: React.FC<AnswerInputProps> = ({ spec, value, onChange, disabled }) => {
  if (spec.kind === "number") {
    return (
      <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
        <label style={{ fontSize: 13, fontWeight: 600, color: "var(--text-secondary)" }}>
          {spec.label || "Respuesta numérica"}
        </label>
        <input
          type="text"
          className="input input-mono"
          style={{ maxWidth: 260 }}
          value={typeof value === "string" ? value : ""}
          onChange={(e) => onChange(e.target.value)}
          placeholder={spec.placeholder || "Ej: -3/4 o 5"}
          disabled={disabled}
          autoComplete="off"
        />
        <span style={{ fontSize: 11.5, color: "var(--text-muted)" }}>
          Admite enteros, fracciones (<code>-3/4</code>) o decimales exactos.
        </span>
      </div>
    );
  }

  if (spec.kind === "vector") {
    const labels = spec.labels || ["x", "y", "z"];
    const arr: string[] = Array.isArray(value) ? value : labels.map(() => "");
    return (
      <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
        <div style={{ fontSize: 13, fontWeight: 600, color: "var(--text-secondary)" }}>
          {spec.label || "Introduce las componentes del vector"}
        </div>
        <div style={{ display: "flex", gap: 10, flexWrap: "wrap", alignItems: "center" }}>
          {labels.map((lbl, idx) => (
            <div key={lbl} style={{ display: "flex", flexDirection: "column", gap: 4 }}>
              <label style={{ fontSize: 12, fontFamily: "var(--font-mono)", color: "var(--accent-cyan)" }}>
                {lbl}
              </label>
              <input
                type="text"
                className="matrix-cell-input"
                style={{ width: 88 }}
                value={arr[idx] ?? ""}
                onChange={(e) => {
                  const next = [...arr];
                  next[idx] = e.target.value;
                  onChange(next);
                }}
                placeholder="0"
                disabled={disabled}
                autoComplete="off"
              />
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (spec.kind === "matrix") {
    const r = spec.rows || 2;
    const c = spec.cols || 2;
    const grid: string[][] =
      Array.isArray(value) && value.length === r
        ? value
        : Array.from({ length: r }, () => Array.from({ length: c }, () => ""));

    return (
      <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
        <div style={{ fontSize: 13, fontWeight: 600, color: "var(--text-secondary)" }}>
          {spec.label || `Matriz ${r}×${c}`}
        </div>
        <div
          className="matrix-grid"
          style={{ gridTemplateColumns: `repeat(${c}, 72px)` }}
        >
          {grid.map((row, ri) =>
            row.map((cell, ci) => (
              <input
                key={`${ri}-${ci}`}
                type="text"
                className="matrix-cell-input"
                value={cell ?? ""}
                onChange={(e) => {
                  const next = grid.map((rw) => [...rw]);
                  next[ri][ci] = e.target.value;
                  onChange(next);
                }}
                placeholder={`a${ri + 1}${ci + 1}`}
                disabled={disabled}
                autoComplete="off"
                aria-label={`Fila ${ri + 1} Columna ${ci + 1}`}
              />
            ))
          )}
        </div>
        <span style={{ fontSize: 11.5, color: "var(--text-muted)" }}>
          Introduce enteros o fracciones exactas (ej. <code>1/2</code>, <code>-3</code>).
        </span>
      </div>
    );
  }

  if (spec.kind === "choice") {
    return (
      <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
        {(spec.options || []).map((opt) => {
          const selected = value === opt.value;
          return (
            <button
              key={opt.value}
              type="button"
              className={`choice-option ${selected ? "selected" : ""}`}
              onClick={() => !disabled && onChange(opt.value)}
              disabled={disabled}
            >
              <span
                style={{
                  width: 18,
                  height: 18,
                  borderRadius: "50%",
                  border: `2px solid ${selected ? "var(--accent-cyan)" : "var(--border-strong)"}`,
                  background: selected ? "var(--accent-cyan)" : "transparent",
                  flexShrink: 0,
                  marginTop: 2,
                }}
              />
              <MathText content={opt.label} />
            </button>
          );
        })}
      </div>
    );
  }

  if (spec.kind === "multi_tf") {
    const map: Record<string, boolean | null> = value && typeof value === "object" ? value : {};
    return (
      <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
        {(spec.items || []).map((item) => {
          const curr = map[item.id];
          return (
            <div
              key={item.id}
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                gap: 14,
                padding: "11px 14px",
                background: "var(--bg-inset)",
                border: "1px solid var(--border-subtle)",
                borderRadius: 8,
                flexWrap: "wrap",
              }}
            >
              <div style={{ flex: 1, minWidth: 220, fontSize: 13.5 }}>
                <MathText content={item.text} />
              </div>
              <div style={{ display: "flex", gap: 6 }}>
                <button
                  type="button"
                  className={`btn btn-sm ${curr === true ? "btn-emerald" : "btn-secondary"}`}
                  onClick={() => !disabled && onChange({ ...map, [item.id]: true })}
                  disabled={disabled}
                >
                  Verdadero
                </button>
                <button
                  type="button"
                  className={`btn btn-sm ${curr === false ? "btn-danger" : "btn-secondary"}`}
                  onClick={() => !disabled && onChange({ ...map, [item.id]: false })}
                  disabled={disabled}
                >
                  Falso
                </button>
              </div>
            </div>
          );
        })}
      </div>
    );
  }

  if (spec.kind === "multi_field") {
    const obj: Record<string, any> = value && typeof value === "object" ? value : {};
    return (
      <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
        {(spec.fields || []).map((f) => (
          <div
            key={f.id}
            style={{
              padding: "12px 14px",
              background: "var(--bg-inset)",
              border: "1px solid var(--border-subtle)",
              borderRadius: 8,
              display: "flex",
              flexDirection: "column",
              gap: 8,
            }}
          >
            <label style={{ fontSize: 13.5, fontWeight: 600, color: "var(--text-primary)" }}>
              {f.label}
            </label>
            {f.type === "number" && (
              <input
                type="text"
                className="input input-mono"
                style={{ maxWidth: 220 }}
                value={obj[f.id] ?? ""}
                onChange={(e) => onChange({ ...obj, [f.id]: e.target.value })}
                placeholder={f.placeholder || "Número o fracción"}
                disabled={disabled}
                autoComplete="off"
              />
            )}
            {f.type === "choice" && (
              <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                {(f.options || []).map((opt) => {
                  const sel = obj[f.id] === opt.value;
                  return (
                    <button
                      key={opt.value}
                      type="button"
                      className={`btn btn-sm ${sel ? "btn-primary" : "btn-secondary"}`}
                      onClick={() => !disabled && onChange({ ...obj, [f.id]: opt.value })}
                      disabled={disabled}
                    >
                      {opt.label}
                    </button>
                  );
                })}
              </div>
            )}
            {f.type === "vector" && (
              <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
                {(f.labels || ["x", "y", "z"]).map((lbl, idx) => {
                  const vecArr: string[] = Array.isArray(obj[f.id])
                    ? obj[f.id]
                    : (f.labels || []).map(() => "");
                  return (
                    <div key={lbl} style={{ display: "flex", alignItems: "center", gap: 5 }}>
                      <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--accent-cyan)" }}>
                        {lbl}:
                      </span>
                      <input
                        type="text"
                        className="matrix-cell-input"
                        style={{ width: 76 }}
                        value={vecArr[idx] ?? ""}
                        onChange={(e) => {
                          const next = [...vecArr];
                          next[idx] = e.target.value;
                          onChange({ ...obj, [f.id]: next });
                        }}
                        placeholder="0"
                        disabled={disabled}
                        autoComplete="off"
                      />
                    </div>
                  );
                })}
              </div>
            )}
          </div>
        ))}
      </div>
    );
  }

  return null;
};
