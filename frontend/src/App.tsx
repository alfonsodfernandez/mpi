import React, { useEffect, useRef, useState } from "react";
import { BrowserRouter, Navigate, Route, Routes, useLocation, useNavigate } from "react-router-dom";
import { apiFetch, setStoredToken } from "./api/client";
import { Sidebar } from "./components/Sidebar";
import { AdminPage } from "./pages/AdminPage";
import { ExamPage } from "./pages/ExamPage";
import { HomePage } from "./pages/HomePage";
import { LoginPage } from "./pages/LoginPage";
import { MatlabLabPage } from "./pages/MatlabLabPage";
import { PracticePage } from "./pages/PracticePage";
import { ProjectPage } from "./pages/ProjectPage";
import { TheoryPage } from "./pages/TheoryPage";
import { UserInfo } from "./types";

const AuthenticatedShell: React.FC<{
  user: UserInfo;
  onLogout: () => void;
}> = ({ user, onLogout }) => {
  const location = useLocation();
  const [isFullscreen, setIsFullscreen] = useState<boolean>(Boolean(document.fullscreenElement));
  const lastActivityRef = useRef<number>(Date.now());

  // Detectar pantalla completa para ocultar la barra lateral durante Modo Blindado
  useEffect(() => {
    const onFs = () => setIsFullscreen(Boolean(document.fullscreenElement));
    document.addEventListener("fullscreenchange", onFs);
    return () => document.removeEventListener("fullscreenchange", onFs);
  }, []);

  // Medición precisa de tiempo efectivo activo (descontando inactividad > 60s o pestaña oculta)
  useEffect(() => {
    const bump = () => {
      lastActivityRef.current = Date.now();
    };
    window.addEventListener("mousemove", bump, { passive: true });
    window.addEventListener("keydown", bump, { passive: true });
    window.addEventListener("click", bump, { passive: true });
    window.addEventListener("scroll", bump, { passive: true });

    const interval = window.setInterval(() => {
      const idleMs = Date.now() - lastActivityRef.current;
      const isActiveNow = !document.hidden && idleMs < 60_000;
      const viewName = location.pathname.replace(/^\//, "") || "home";
      void apiFetch("/api/auth/heartbeat", {
        method: "POST",
        body: JSON.stringify({
          delta_seconds: isActiveNow ? 15 : 0,
          is_active: isActiveNow,
          current_view: viewName,
        }),
      }).catch(() => {});
    }, 15_000);

    return () => {
      window.clearInterval(interval);
      window.removeEventListener("mousemove", bump);
      window.removeEventListener("keydown", bump);
      window.removeEventListener("click", bump);
      window.removeEventListener("scroll", bump);
    };
  }, [location.pathname]);

  const hideSidebar = isFullscreen && (location.pathname.startsWith("/ejercicios") || location.pathname.startsWith("/examenes"));

  return (
    <div className="app-shell">
      {!hideSidebar && <Sidebar user={user} onLogout={onLogout} />}
      <main className={hideSidebar ? "" : "main-content"} style={hideSidebar ? { flex: 1, width: "100%" } : undefined}>
        <Routes>
          {user.role === "admin" ? (
            <>
              <Route path="/admin" element={<AdminPage />} />
              <Route path="/teoria" element={<TheoryPage />} />
              <Route path="/matlab" element={<MatlabLabPage />} />
              <Route path="/proyecto" element={<ProjectPage />} />
              <Route path="*" element={<Navigate to="/admin" replace />} />
            </>
          ) : (
            <>
              <Route path="/" element={<HomePage />} />
              <Route path="/teoria" element={<TheoryPage />} />
              <Route path="/ejercicios" element={<PracticePage user={user} />} />
              <Route path="/examenes" element={<ExamPage user={user} />} />
              <Route path="/matlab" element={<MatlabLabPage />} />
              <Route path="/proyecto" element={<ProjectPage />} />
              <Route path="/admin" element={<Navigate to="/" replace />} />
              <Route path="*" element={<Navigate to="/" replace />} />
            </>
          )}
        </Routes>
      </main>
    </div>
  );
};

const RootRouter: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const [user, setUser] = useState<UserInfo | null>(null);
  const [checking, setChecking] = useState(true);

  useEffect(() => {
    apiFetch<UserInfo>("/api/auth/me")
      .then((u) => setUser(u))
      .catch(() => {
        setStoredToken(null);
        setUser(null);
      })
      .finally(() => setChecking(false));
  }, []);

  const handleAuthenticated = (u: UserInfo) => {
    setUser(u);
    if (u.role === "admin") {
      navigate("/admin", { replace: true });
    } else {
      navigate("/", { replace: true });
    }
  };

  const handleLogout = async () => {
    try {
      await apiFetch("/api/auth/logout", { method: "POST" });
    } catch {
      // ignore
    }
    setStoredToken(null);
    setUser(null);
    navigate("/", { replace: true });
  };

  if (checking) {
    return (
      <div className="login-shell">
        <div className="panel" style={{ padding: "18px 26px", fontFamily: "var(--font-mono)", fontSize: 13 }}>
          Verificando sesión segura...
        </div>
      </div>
    );
  }

  if (!user) {
    const isAdminRoute = location.pathname.startsWith("/admin");
    return <LoginPage adminPortal={isAdminRoute} onAuthenticated={handleAuthenticated} />;
  }

  return <AuthenticatedShell user={user} onLogout={handleLogout} />;
};

export const App: React.FC = () => (
  <BrowserRouter>
    <RootRouter />
  </BrowserRouter>
);

export default App;
