"""Configuración central de la Plataforma MPI-I (UFV)."""
from __future__ import annotations

import os
from pathlib import Path


def _env_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


REPO_ROOT = Path(__file__).resolve().parents[2]
CONTEXT_DIR = Path(os.getenv("CONTEXT_DIR", str(REPO_ROOT / "_contexto_mpi")))
FRONTEND_DIST_DIR = Path(os.getenv("FRONTEND_DIST_DIR", str(REPO_ROOT / "frontend" / "dist")))
DATA_DIR = Path(os.getenv("DATA_DIR", str(REPO_ROOT / "data")))
DATA_DIR.mkdir(parents=True, exist_ok=True)


class Settings:
    APP_NAME: str = "MPI-I · Entorno Blindado de Álgebra Lineal (UFV)"
    APP_VERSION: str = "1.0.0"

    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-mpi-ufv-secret-key-change-in-production-9f8e7d6c")
    SESSION_EXPIRE_HOURS: int = int(os.getenv("SESSION_EXPIRE_HOURS", "12"))

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{(DATA_DIR / 'mpi_platform.db').as_posix()}",
    )

    PABLO_USERNAME: str = os.getenv("PABLO_USERNAME", "pablo")
    PABLO_PASSWORD: str = os.getenv("PABLO_PASSWORD", "pablo2026")
    PABLO_DISPLAY_NAME: str = os.getenv("PABLO_DISPLAY_NAME", "Pablo")

    ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME", "profesor")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "profesor2026")
    ADMIN_DISPLAY_NAME: str = os.getenv("ADMIN_DISPLAY_NAME", "Profesor MPI-I")

    TRUST_PROXY_HEADERS: bool = _env_bool("TRUST_PROXY_HEADERS", True)
    COOKIE_SECURE: bool = _env_bool("COOKIE_SECURE", False)
    CORS_ORIGINS: list[str] = [
        o.strip() for o in os.getenv("CORS_ORIGINS", "").split(",") if o.strip()
    ]


settings = Settings()
