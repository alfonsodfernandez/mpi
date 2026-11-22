import React, { useEffect, useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import {
  BookOpen,
  CheckSquare,
  ChevronDown,
  ChevronRight,
  Cpu,
  FileText,
  Save,
  Search,
  Square,
} from "lucide-react";
import { apiFetch } from "../api/client";
import { MathText } from "../components/MathText";

interface TheoryModule {
  id: string;
  order: number;
  topic_filter: string;
  title: string;
  subtitle: string;
  source_files: string[];
  definitions: { term: string; body_md: string }[];
  theorems: { name: string; body_md: string }[];
  worked_examples: { title: string; problem_md: string; steps_md: string[] }[];
  raw_sections: { title: string; source: string; content_md: string }[];
}

interface ChecklistGroup {
  topic_key: string;
  title: string;
  items: { id: string; text: string; completed: boolean }[];
}

export const TheoryPage: React.FC = () => {
  const navigate = useNavigate();
  const [searchParams, setSearchParams] = useSearchParams();
  const [modules, setModules] = useState<TheoryModule[]>([]);
  const [overview, setOverview] = useState<any>(null);
  const [checklist, setChecklist] = useState<ChecklistGroup[]>([]);
  const [notesMap, setNotesMap] = useState<Record<string, { content: string; updated_at?: string }>>({});
  const [activeTab, setActiveTab] = useState<string>(searchParams.get("modulo") || "guia");
  const [notePreview, setNotePreview] = useState(false);
  const [savingNote, setSavingNote] = useState(false);
  const [savedToast, setSavedToast] = useState<string | null>(null);
  const [openExamples, setOpenExamples] = useState<Record<string, boolean>>({});
  const [openRaw, setOpenRaw] = useState<Record<string, boolean>>({});
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState<any[]>([]);

  useEffect(() => {
    Promise.all([
      apiFetch<{ modules: TheoryModule[] }>("/api/content/theory"),
      apiFetch<any>("/api/content/overview"),
      apiFetch<{ notes: Record<string, { content: string; updated_at: string }> }>("/api/notes"),
    ]).then(([t, ov, n]) => {
      setModules(t.modules);
      setOverview(ov.course_meta);
      setChecklist(ov.checklist);
      setNotesMap(n.notes || {});
    });
  }, []);

  useEffect(() => {
    const modParam = searchParams.get("modulo");
    if (modParam) setActiveTab(modParam);
  }, [searchParams]);

  const handleSearch = async (q: string) => {
    setSearchQuery(q);
    if (q.trim().length < 2) {
      setSearchResults([]);
      return;
    }
    const res = await apiFetch<{ results: any[] }>(`/api/content/search?q=${encodeURIComponent(q)}`);
    setSearchResults(res.results || []);
  };

  const handleToggleChecklist = async (itemId: string, current: boolean) => {
    const next = !current;
    setChecklist((prev) =>
      prev.map((g) => ({
        ...g,
        items: g.items.map((it) => (it.id === itemId ? { ...it, completed: next } : it)),
      }))
    );
    await apiFetch(`/api/checklist/${itemId}`, {
      method: "PUT",
      body: JSON.stringify({ completed: next }),
    });
  };

  const currentNoteKey = activeTab;
  const currentNoteContent = notesMap[currentNoteKey]?.content || "";

  const handleSaveNote = async () => {
    setSavingNote(true);
    try {
      const res = await apiFetch<{ content: string; updated_at: string }>(`/api/notes/${currentNoteKey}`, {
        method: "PUT",
        body: JSON.stringify({ content: currentNoteContent }),
      });
      setNotesMap((prev) => ({ ...prev, [currentNoteKey]: res }));
      setSavedToast("Apunte guardado");
      setTimeout(() => setSavedToast(null), 2000);
    } finally {
      setSavingNote(false);
    }
  };

  const activeModule = modules.find((m) => m.id === activeTab);

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
      <div className="page-header">
        <div>
          <h1 className="page-title">Teoría Interactiva · Álgebra Lineal</h1>
          <p className="page-subtitle">
            Temario íntegro indexado desde <code>_contexto_mpi/00..05</code> con definiciones, teoremas, ejemplos paso a paso y bloc de notas.
          </p>
        </div>
        <div style={{ position: "relative", width: 320, maxWidth: "100%" }}>
          <Search size={15} style={{ position: "absolute", left: 11, top: "50%", transform: "translateY(-50%)", color: "var(--text-muted)" }} />
          <input
            type="text"
            className="input"
            style={{ paddingLeft: 34 }}
            placeholder="Buscar teorema, definición, MATLAB..."
            value={searchQuery}
            onChange={(e) => handleSearch(e.target.value)}
          />
          {searchResults.length > 0 && (
            <div
              className="panel-elevated"
              style={{
                position: "absolute",
                top: "calc(100% + 6px)",
                right: 0,
                width: 420,
                maxWidth: "90vw",
                maxHeight: 360,
                overflowY: "auto",
                zIndex: 50,
                padding: 12,
                display: "flex",
                flexDirection: "column",
                gap: 8,
              }}
            >
              {searchResults.map((hit, i) => (
                <button
                  key={i}
                  type="button"
                  className="choice-option"
                  onClick={() => {
                    setSearchQuery("");
                    setSearchResults([]);
                    if (hit.route.startsWith("/teoria?modulo=")) {
                      const mid = hit.route.split("=")[1];
                      setActiveTab(mid);
                      setSearchParams({ modulo: mid });
                    } else {
                      navigate(hit.route);
                    }
                  }}
                >
                  <div>
                    <div style={{ fontSize: 11, fontFamily: "var(--font-mono)", color: "var(--accent-cyan)" }}>
                      {hit.kind}
                    </div>
                    <div style={{ fontWeight: 600, fontSize: 13.5 }}>{hit.title}</div>
                  </div>
                </button>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Pestañas de bloques */}
      <div className="tabs">
        <button
          type="button"
          className={`tab-btn ${activeTab === "guia" ? "active" : ""}`}
          onClick={() => {
            setActiveTab("guia");
            setSearchParams({});
          }}
        >
          00–01 · Guía y Checklist
        </button>
        {modules.map((m) => (
          <button
            key={m.id}
            type="button"
            className={`tab-btn ${activeTab === m.id ? "active" : ""}`}
            onClick={() => {
              setActiveTab(m.id);
              setSearchParams({ modulo: m.id });
            }}
          >
            {m.title}
          </button>
        ))}
      </div>

      <div className="split-workspace">
        {/* Columna principal de teoría */}
        <div style={{ display: "flex", flexDirection: "column", gap: 18 }}>
          {activeTab === "guia" && overview && (
            <>
              <div className="panel">
                <h2 className="panel-title">
                  <BookOpen size={17} style={{ color: "var(--accent-cyan)" }} />
                  Sistema de Evaluación y Guía Docente ({overview.code} · {overview.ects} ECTS)
                </h2>
                <div className="grid-3" style={{ marginBottom: 14 }}>
                  {overview.evaluation.map((ev: any) => (
                    <div key={ev.part} className="kpi-card" style={{ padding: 14 }}>
                      <div style={{ fontSize: 12, color: "var(--text-secondary)", fontWeight: 600 }}>{ev.part}</div>
                      <div style={{ fontSize: 22, fontFamily: "var(--font-mono)", fontWeight: 700, color: "var(--accent-cyan)", marginTop: 4 }}>
                        {ev.weight}
                      </div>
                      <div style={{ fontSize: 12, color: "var(--text-muted)", marginTop: 2 }}>{ev.min}</div>
                    </div>
                  ))}
                </div>
                <div style={{ fontSize: 13, color: "var(--text-secondary)" }}>
                  <strong>Bibliografía:</strong> {overview.bibliography.join(" | ")}
                </div>
              </div>

              <div className="panel">
                <h2 className="panel-title">Checklist Oficial: «Qué hay que saber de Álgebra»</h2>
                <p style={{ margin: "0 0 14px", fontSize: 13, color: "var(--text-secondary)" }}>
                  Marca los conceptos que ya dominas (se guarda automáticamente y el profesor ve tu progreso).
                </p>
                <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
                  {checklist.map((group) => (
                    <div key={group.topic_key}>
                      <div style={{ fontWeight: 700, fontSize: 14, color: "var(--accent-amber)", marginBottom: 8 }}>
                        {group.title}
                      </div>
                      <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
                        {group.items.map((item) => (
                          <button
                            key={item.id}
                            type="button"
                            onClick={() => handleToggleChecklist(item.id, item.completed)}
                            style={{
                              display: "flex",
                              alignItems: "flex-start",
                              gap: 10,
                              padding: "9px 12px",
                              background: item.completed ? "rgba(16, 185, 129, 0.08)" : "var(--bg-inset)",
                              border: `1px solid ${item.completed ? "rgba(16, 185, 129, 0.35)" : "var(--border-subtle)"}`,
                              borderRadius: 7,
                              color: item.completed ? "#a7f3d0" : "var(--text-primary)",
                              cursor: "pointer",
                              textAlign: "left",
                              fontSize: 13.5,
                            }}
                          >
                            {item.completed ? (
                              <CheckSquare size={17} style={{ color: "var(--accent-emerald)", flexShrink: 0, marginTop: 2 }} />
                            ) : (
                              <Square size={17} style={{ color: "var(--text-muted)", flexShrink: 0, marginTop: 2 }} />
                            )}
                            <span>{item.text}</span>
                          </button>
                        ))}
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {overview.grossman_syllabus && (
                <div className="panel">
                  <h2 className="panel-title">Secciones del Libro Grossman (8.ª ed.) que entran</h2>
                  <pre
                    style={{
                      margin: 0,
                      padding: 14,
                      background: "var(--bg-inset)",
                      borderRadius: 8,
                      border: "1px solid var(--border-subtle)",
                      fontFamily: "var(--font-mono)",
                      fontSize: 12.5,
                      color: "var(--text-secondary)",
                      overflowX: "auto",
                      maxHeight: 340,
                    }}
                  >
                    {overview.grossman_syllabus}
                  </pre>
                </div>
              )}
            </>
          )}

          {activeModule && (
            <>
              <div className="panel" style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 12 }}>
                <div>
                  <h2 style={{ margin: 0, fontSize: 19 }}>{activeModule.title}</h2>
                  <p style={{ margin: "4px 0 0", fontSize: 13.5, color: "var(--text-secondary)" }}>
                    {activeModule.subtitle}
                  </p>
                </div>
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={() => navigate(`/ejercicios?topic=${activeModule.topic_filter}`)}
                >
                  <Cpu size={15} /> Practicar este bloque
                </button>
              </div>

              {/* Definiciones clave */}
              <div className="panel">
                <h3 className="panel-title" style={{ color: "var(--accent-cyan)" }}>
                  Definiciones Fundamentales
                </h3>
                <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
                  {activeModule.definitions.map((d, i) => (
                    <div
                      key={i}
                      style={{
                        padding: "13px 15px",
                        background: "var(--bg-inset)",
                        borderLeft: "3px solid var(--accent-cyan)",
                        borderRadius: "0 8px 8px 0",
                      }}
                    >
                      <div style={{ fontWeight: 700, fontSize: 14.5, marginBottom: 6 }}>
                        <MathText content={d.term} />
                      </div>
                      <MathText content={d.body_md} />
                    </div>
                  ))}
                </div>
              </div>

              {/* Teoremas Clave */}
              <div className="panel">
                <h3 className="panel-title" style={{ color: "var(--accent-amber)" }}>
                  Teoremas y Criterios de Examen
                </h3>
                <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
                  {activeModule.theorems.map((t, i) => (
                    <div
                      key={i}
                      style={{
                        padding: "13px 15px",
                        background: "rgba(245, 158, 11, 0.05)",
                        border: "1px solid rgba(245, 158, 11, 0.24)",
                        borderRadius: 8,
                      }}
                    >
                      <div style={{ fontWeight: 700, fontSize: 14.5, color: "#fcd34d", marginBottom: 6 }}>
                        {t.name}
                      </div>
                      <MathText content={t.body_md} />
                    </div>
                  ))}
                </div>
              </div>

              {/* Ejemplos resueltos paso a paso */}
              <div className="panel">
                <h3 className="panel-title" style={{ color: "var(--accent-emerald)" }}>
                  Ejemplos Resueltos Paso a Paso
                </h3>
                <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
                  {activeModule.worked_examples.map((ex, idx) => {
                    const key = `${activeModule.id}-ex-${idx}`;
                    const isOpen = !!openExamples[key];
                    return (
                      <div
                        key={key}
                        style={{
                          background: "var(--bg-inset)",
                          border: "1px solid var(--border-subtle)",
                          borderRadius: 8,
                          padding: 15,
                        }}
                      >
                        <div style={{ fontWeight: 700, fontSize: 14.5, marginBottom: 8 }}>{ex.title}</div>
                        <MathText content={ex.problem_md} />
                        <button
                          type="button"
                          className="btn btn-sm btn-secondary"
                          style={{ marginTop: 10 }}
                          onClick={() => setOpenExamples((p) => ({ ...p, [key]: !isOpen }))}
                        >
                          {isOpen ? <ChevronDown size={14} /> : <ChevronRight size={14} />}
                          {isOpen ? "Ocultar resolución paso a paso" : "Ver resolución paso a paso"}
                        </button>
                        {isOpen && (
                          <ol style={{ margin: "12px 0 0 20px", padding: 0, display: "flex", flexDirection: "column", gap: 8 }}>
                            {ex.steps_md.map((st, si) => (
                              <li key={si}>
                                <MathText content={st} />
                              </li>
                            ))}
                          </ol>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>

              {/* Transcripciones completas de pizarras y boletines de _contexto_mpi */}
              {activeModule.raw_sections.length > 0 && (
                <div className="panel">
                  <h3 className="panel-title">
                    <FileText size={16} /> Pizarras y Apuntes Originales de Clase (UFV)
                  </h3>
                  <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                    {activeModule.raw_sections.map((sec, idx) => {
                      const key = `${activeModule.id}-raw-${idx}`;
                      const isOpen = !!openRaw[key];
                      return (
                        <div
                          key={key}
                          style={{
                            border: "1px solid var(--border-subtle)",
                            borderRadius: 8,
                            overflow: "hidden",
                          }}
                        >
                          <button
                            type="button"
                            onClick={() => setOpenRaw((p) => ({ ...p, [key]: !isOpen }))}
                            style={{
                              width: "100%",
                              display: "flex",
                              justifyContent: "space-between",
                              alignItems: "center",
                              padding: "11px 14px",
                              background: "var(--bg-inset)",
                              border: "none",
                              color: "var(--text-primary)",
                              cursor: "pointer",
                              fontWeight: 600,
                              fontSize: 13.5,
                              textAlign: "left",
                            }}
                          >
                            <span>{sec.title}</span>
                            {isOpen ? <ChevronDown size={16} /> : <ChevronRight size={16} />}
                          </button>
                          {isOpen && (
                            <div style={{ padding: 16, borderTop: "1px solid var(--border-subtle)", maxHeight: 540, overflowY: "auto" }}>
                              {sec.source && (
                                <div style={{ fontSize: 11.5, fontFamily: "var(--font-mono)", color: "var(--text-muted)", marginBottom: 10 }}>
                                  Fuente: {sec.source}
                                </div>
                              )}
                              <MathText content={sec.content_md} />
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}
            </>
          )}
        </div>

        {/* Columna derecha fija: Bloc de Notas Rápido Integrado con soporte KaTeX */}
        <div className="panel" style={{ position: "sticky", top: 20, display: "flex", flexDirection: "column", gap: 12 }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", gap: 8 }}>
            <h3 className="panel-title" style={{ margin: 0 }}>
              Bloc de Notas ({activeTab === "guia" ? "General" : activeModule?.title.split("·")[0]})
            </h3>
            <div style={{ display: "flex", gap: 6 }}>
              <button
                type="button"
                className={`btn btn-sm ${!notePreview ? "btn-primary" : "btn-secondary"}`}
                onClick={() => setNotePreview(false)}
              >
                Editar
              </button>
              <button
                type="button"
                className={`btn btn-sm ${notePreview ? "btn-primary" : "btn-secondary"}`}
                onClick={() => setNotePreview(true)}
              >
                Vista KaTeX
              </button>
            </div>
          </div>

          <p style={{ margin: 0, fontSize: 12, color: "var(--text-muted)" }}>
            Anota trucos, dudas y fórmulas con LaTeX (<code>$A=PDP^{"{-1}"}$</code>). Se guarda en tu cuenta.
          </p>

          {notePreview ? (
            <div
              style={{
                minHeight: 320,
                padding: 14,
                background: "var(--bg-inset)",
                border: "1px solid var(--border-subtle)",
                borderRadius: 8,
                overflowY: "auto",
              }}
            >
              {currentNoteContent.trim() ? (
                <MathText content={currentNoteContent} />
              ) : (
                <span style={{ color: "var(--text-muted)", fontSize: 13 }}>Sin notas todavía en este bloque.</span>
              )}
            </div>
          ) : (
            <textarea
              className="textarea input-mono"
              rows={15}
              value={currentNoteContent}
              onChange={(e) =>
                setNotesMap((prev) => ({
                  ...prev,
                  [currentNoteKey]: { ...prev[currentNoteKey], content: e.target.value },
                }))
              }
              placeholder={"Ej:\n- Para discutir por Gauss sin Rouché: buscar pivotes.\n- $A = LU$ normalizada lleva 1s en la diagonal de $L$.\n- Diagonalizable sii $m_g(\\lambda) = m_a(\\lambda)$."}
            />
          )}

          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <span style={{ fontSize: 12, color: "var(--accent-emerald)" }}>{savedToast || ""}</span>
            <button type="button" className="btn btn-primary btn-sm" onClick={handleSaveNote} disabled={savingNote}>
              <Save size={14} /> {savingNote ? "Guardando..." : "Guardar nota"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
