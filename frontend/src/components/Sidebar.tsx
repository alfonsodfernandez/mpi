import React from "react";
import { NavLink } from "react-router-dom";
import {
  Activity,
  BookOpen,
  Cpu,
  FileCheck2,
  Home,
  LogOut,
  Network,
  Shield,
  Terminal,
} from "lucide-react";
import { UserInfo } from "../types";

interface SidebarProps {
  user: UserInfo;
  onLogout: () => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ user, onLogout }) => {
  const isAdmin = user.role === "admin";

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <div className="brand-row">
          <div className="brand-mark">Aλ</div>
          <div>
            <div className="brand-title">MPI-I · Álgebra</div>
            <div className="brand-sub">UFV · 5666 · Entorno Blindado</div>
          </div>
        </div>
      </div>

      <nav className="sidebar-nav" aria-label="Navegación principal">
        {isAdmin ? (
          <>
            <div className="nav-section-label">Auditoría Docente</div>
            <NavLink to="/admin" className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
              <Shield size={16} /> Panel de Control (/admin)
            </NavLink>
            <div className="nav-section-label">Vista Previa Temario</div>
            <NavLink to="/teoria" className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
              <BookOpen size={16} /> Teoría Interactiva
            </NavLink>
            <NavLink to="/matlab" className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
              <Terminal size={16} /> Laboratorio MATLAB
            </NavLink>
            <NavLink to="/proyecto" className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
              <Network size={16} /> Proyecto Red Logística
            </NavLink>
          </>
        ) : (
          <>
            <div className="nav-section-label">Estudio</div>
            <NavLink to="/" end className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
              <Home size={16} /> Resumen de Pablo
            </NavLink>
            <NavLink to="/teoria" className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
              <BookOpen size={16} /> Teoría Interactiva
            </NavLink>

            <div className="nav-section-label">Entrenamiento Blindado</div>
            <NavLink to="/ejercicios" className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
              <Cpu size={16} /> Ejercicios Infinitos
            </NavLink>
            <NavLink to="/examenes" className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
              <FileCheck2 size={16} /> Simulador de Exámenes
            </NavLink>

            <div className="nav-section-label">Prácticas y Proyecto</div>
            <NavLink to="/matlab" className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
              <Terminal size={16} /> Laboratorio MATLAB
            </NavLink>
            <NavLink to="/proyecto" className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}>
              <Network size={16} /> Proyecto Red Logística
            </NavLink>
          </>
        )}
      </nav>

      <div className="sidebar-footer">
        <div className="user-badge">
          <div className="user-meta">
            <span className="user-name">{user.display_name}</span>
            <span className="user-role">
              <Activity size={10} style={{ verticalAlign: "middle", marginRight: 4 }} />
              {isAdmin ? "MODO PROFESOR" : "SESIÓN AUDITADA"}
            </span>
          </div>
          <button
            type="button"
            className="btn btn-sm btn-ghost"
            onClick={onLogout}
            title="Cerrar sesión"
          >
            <LogOut size={15} />
          </button>
        </div>
      </div>
    </aside>
  );
};
