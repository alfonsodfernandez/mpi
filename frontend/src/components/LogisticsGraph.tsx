import React, { useState } from "react";
import { LogisticsAnalysis } from "../types";

interface LogisticsGraphProps {
  analysis: LogisticsAnalysis;
  onSelectDisabledCenter: (name: string | null) => void;
}

export const LogisticsGraph: React.FC<LogisticsGraphProps> = ({
  analysis,
  onSelectDisabledCenter,
}) => {
  const [hovered, setHovered] = useState<string | null>(null);

  const posMap = new Map(analysis.centers_all.map((c) => [c.name, c]));
  const metricMap = new Map(analysis.nodes.map((n) => [n.name, n]));

  // Coordenadas en viewBox 0..760 x 0..460
  const toXY = (c: { x: number; y: number }) => ({
    x: 40 + (c.x / 100) * 680,
    y: 35 + (c.y / 100) * 390,
  });

  const renderEdge = (
    edge: { source: string; target: string; flow: number },
    removed: boolean
  ) => {
    const s = posMap.get(edge.source);
    const t = posMap.get(edge.target);
    if (!s || !t) return null;
    const p1 = toXY(s);
    const p2 = toXY(t);
    const dx = p2.x - p1.x;
    const dy = p2.y - p1.y;
    const dist = Math.hypot(dx, dy) || 1;
    // Curvar ligeramente para distinguir rutas bidireccionales (ej. Madrid <-> Valencia)
    const mx = (p1.x + p2.x) / 2 - (dy / dist) * 16;
    const my = (p1.y + p2.y) / 2 + (dx / dist) * 16;

    // Acortar extremo para que la flecha termine en el borde del círculo
    const ux = (p2.x - mx) / (Math.hypot(p2.x - mx, p2.y - my) || 1);
    const uy = (p2.y - my) / (Math.hypot(p2.x - mx, p2.y - my) || 1);
    const endX = p2.x - ux * 22;
    const endY = p2.y - uy * 22;

    const highlighted = hovered && (edge.source === hovered || edge.target === hovered);
    const strokeW = Math.max(1.3, (edge.flow / 850) * 3.8);

    return (
      <g key={`${edge.source}-${edge.target}-${removed ? "rm" : "ok"}`}>
        <path
          d={`M ${p1.x} ${p1.y} Q ${mx} ${my} ${endX} ${endY}`}
          fill="none"
          stroke={
            removed
              ? "rgba(239, 68, 68, 0.32)"
              : highlighted
              ? "#fbbf24"
              : "rgba(56, 189, 248, 0.42)"
          }
          strokeWidth={highlighted ? strokeW + 1 : strokeW}
          strokeDasharray={removed ? "5 5" : undefined}
          markerEnd={removed ? "url(#arrow-red)" : highlighted ? "url(#arrow-amber)" : "url(#arrow-cyan)"}
        />
        {(highlighted || removed) && (
          <text
            x={mx}
            y={my - 4}
            textAnchor="middle"
            fill={removed ? "#fca5a5" : "#fde68a"}
            fontSize="10.5"
            fontFamily="JetBrains Mono, monospace"
            fontWeight={600}
          >
            {edge.flow}t
          </text>
        )}
      </g>
    );
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 8 }}>
        <div style={{ fontSize: 13, color: "var(--text-secondary)" }}>
          Haz clic en cualquier centro para simular su caída (o usa el escenario oficial <strong>DANA Valencia</strong>).
        </div>
        <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
          <button
            type="button"
            className={`btn btn-sm ${!analysis.disabled_center ? "btn-primary" : "btn-secondary"}`}
            onClick={() => onSelectDisabledCenter(null)}
          >
            Red Normal (12 centros)
          </button>
          <button
            type="button"
            className={`btn btn-sm ${analysis.disabled_center === "Valencia" ? "btn-danger" : "btn-secondary"}`}
            onClick={() => onSelectDisabledCenter("Valencia")}
          >
            Simular DANA Valencia (Reto 6)
          </button>
        </div>
      </div>

      <div
        style={{
          background: "#090d14",
          border: "1px solid var(--border-subtle)",
          borderRadius: 10,
          overflow: "hidden",
        }}
      >
        <svg viewBox="0 0 760 460" style={{ width: "100%", height: "auto", display: "block" }}>
          <defs>
            <marker id="arrow-cyan" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 10 5 L 0 9 z" fill="rgba(56, 189, 248, 0.75)" />
            </marker>
            <marker id="arrow-amber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 10 5 L 0 9 z" fill="#fbbf24" />
            </marker>
            <marker id="arrow-red" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 10 5 L 0 9 z" fill="rgba(239, 68, 68, 0.5)" />
            </marker>
          </defs>

          {/* Aristas eliminadas primero */}
          {analysis.removed_flows.map((f) => renderEdge(f, true))}
          {/* Aristas activas */}
          {analysis.active_flows.map((f) => renderEdge(f, false))}

          {/* Nodos */}
          {analysis.centers_all.map((c) => {
            const p = toXY(c);
            const isDisabled = analysis.disabled_center === c.name;
            const m = metricMap.get(c.name);
            const isIsolated = m?.is_isolated;
            const radius = isDisabled ? 18 : 14 + Math.min(11, (m?.pagerank_pct || 4) * 0.48);

            let fill = "#1e293b";
            let stroke = "#38bdf8";
            if (isDisabled) {
              fill = "rgba(239, 68, 68, 0.2)";
              stroke = "#ef4444";
            } else if (isIsolated) {
              fill = "rgba(245, 158, 11, 0.18)";
              stroke = "#f59e0b";
            } else if (c.type === "hub nacional") {
              fill = "#1e3a5f";
              stroke = "#38bdf8";
            } else if (c.type === "hub regional") {
              fill = "#13302b";
              stroke = "#10b981";
            }

            return (
              <g
                key={c.name}
                style={{ cursor: "pointer" }}
                onMouseEnter={() => setHovered(c.name)}
                onMouseLeave={() => setHovered(null)}
                onClick={() => onSelectDisabledCenter(isDisabled ? null : c.name)}
              >
                <circle cx={p.x} cy={p.y} r={radius} fill={fill} stroke={stroke} strokeWidth={hovered === c.name ? 3 : 2} />
                <text
                  x={p.x}
                  y={p.y + 4}
                  textAnchor="middle"
                  fill={isDisabled ? "#fca5a5" : "#f8fafc"}
                  fontSize="11"
                  fontFamily="JetBrains Mono, monospace"
                  fontWeight={700}
                >
                  {isDisabled ? "✕" : c.code}
                </text>
                <text
                  x={p.x}
                  y={p.y + radius + 14}
                  textAnchor="middle"
                  fill={isDisabled ? "#f87171" : isIsolated ? "#fbbf24" : "#cbd5e1"}
                  fontSize="11.5"
                  fontWeight={600}
                >
                  {c.name}
                  {m ? ` (${m.pagerank_pct}%)` : " [INOP]"}
                </text>
              </g>
            );
          })}
        </svg>
      </div>

      <div style={{ display: "flex", gap: 16, flexWrap: "wrap", fontSize: 12, color: "var(--text-secondary)" }}>
        <span><strong style={{ color: "#38bdf8" }}>●</strong> Hub Nacional</span>
        <span><strong style={{ color: "#10b981" }}>●</strong> Hub Regional</span>
        <span><strong style={{ color: "#94a3b8" }}>●</strong> Distribución</span>
        <span><strong style={{ color: "#f59e0b" }}>●</strong> Nodo aislado tras caída</span>
        <span><strong style={{ color: "#ef4444" }}>✕</strong> Centro inoperativo</span>
      </div>
    </div>
  );
};
