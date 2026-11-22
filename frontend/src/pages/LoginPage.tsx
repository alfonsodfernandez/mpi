import React, { useState } from "react";
import { Lock, Shield, User as UserIcon } from "lucide-react";
import { apiFetch, setStoredToken } from "../api/client";
import { UserInfo } from "../types";

interface LoginPageProps {
  adminPortal?: boolean;
  onAuthenticated: (user: UserInfo) => void;
}

export const LoginPage: React.FC<LoginPageProps> = ({ adminPortal = false, onAuthenticated }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const res = await apiFetch<{ token: string; user: UserInfo }>("/api/auth/login", {
        method: "POST",
        body: JSON.stringify({ username: username.trim(), password }),
      });
      if (adminPortal && res.user.role !== "admin") {
        setError("Esta ruta (/admin) es de acceso exclusivo para el profesor.");
        setLoading(false);
        return;
      }
      setStoredToken(res.token);
      onAuthenticated(res.user);
    } catch (err: any) {
      setError(err?.message || "No se pudo iniciar sesión.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-shell">
      <div className="login-card">
        <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 22 }}>
          <div className="brand-mark" style={{ width: 42, height: 42, fontSize: 16 }}>
            {adminPortal ? <Shield size={20} /> : "Aλ"}
          </div>
          <div>
            <h1 style={{ margin: 0, fontSize: 20, letterSpacing: "-0.02em" }}>
              {adminPortal ? "Panel del Profesor (/admin)" : "MPI-I · Entorno de Estudio"}
            </h1>
            <div style={{ fontSize: 12.5, color: "var(--text-muted)", fontFamily: "var(--font-mono)" }}>
              Álgebra Lineal · UFV Código 5666
            </div>
          </div>
        </div>

        <p style={{ margin: "0 0 20px", fontSize: 13.5, color: "var(--text-secondary)" }}>
          {adminPortal
            ? "Introduce tus credenciales docentes para auditar sesiones, tiempo efectivo, rendimiento académico e infracciones."
            : "Plataforma exclusiva de entrenamiento de alto rendimiento. Todas las sesiones, tiempos y pruebas quedan registradas."}
        </p>

        <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          <div>
            <label style={{ display: "block", fontSize: 12.5, fontWeight: 600, color: "var(--text-secondary)", marginBottom: 6 }}>
              Usuario
            </label>
            <div style={{ position: "relative" }}>
              <UserIcon
                size={15}
                style={{ position: "absolute", left: 11, top: "50%", transform: "translateY(-50%)", color: "var(--text-muted)" }}
              />
              <input
                type="text"
                className="input"
                style={{ paddingLeft: 34 }}
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder={adminPortal ? "profesor" : "pablo"}
                autoComplete="username"
                required
              />
            </div>
          </div>

          <div>
            <label style={{ display: "block", fontSize: 12.5, fontWeight: 600, color: "var(--text-secondary)", marginBottom: 6 }}>
              Contraseña
            </label>
            <div style={{ position: "relative" }}>
              <Lock
                size={15}
                style={{ position: "absolute", left: 11, top: "50%", transform: "translateY(-50%)", color: "var(--text-muted)" }}
              />
              <input
                type="password"
                className="input"
                style={{ paddingLeft: 34 }}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••••••"
                autoComplete="current-password"
                required
              />
            </div>
          </div>

          {error && (
            <div
              style={{
                padding: "10px 12px",
                borderRadius: 6,
                background: "rgba(239, 68, 68, 0.14)",
                border: "1px solid rgba(239, 68, 68, 0.35)",
                color: "#fca5a5",
                fontSize: 13,
              }}
            >
              {error}
            </div>
          )}

          <button type="submit" className="btn btn-primary" style={{ marginTop: 6, padding: "11px 16px" }} disabled={loading}>
            {loading ? "Verificando acceso..." : adminPortal ? "Acceder al Panel Docente" : "Iniciar Sesión de Estudio"}
          </button>
        </form>

        <div
          style={{
            marginTop: 20,
            paddingTop: 16,
            borderTop: "1px solid var(--border-subtle)",
            display: "flex",
            justifyContent: "space-between",
            fontSize: 12,
            color: "var(--text-muted)",
          }}
        >
          <span>Conexión segura · Sesión auditada</span>
          {adminPortal ? (
            <a href="/">Acceso alumno</a>
          ) : (
            <a href="/admin">Acceso profesor (/admin)</a>
          )}
        </div>
      </div>
    </div>
  );
};
