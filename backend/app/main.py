"""Aplicación principal FastAPI: seguridad, inicialización DB/usuarios, API y servicio del SPA Frontend."""
from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from .auth import ensure_default_users
from .config import FRONTEND_DIST_DIR, settings
from .content.indexer import get_course_index
from .database import Base, SessionLocal, engine
from .routers import (
    admin_router,
    auth_router,
    content_router,
    exams_router,
    exercises_router,
    security_router,
)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        ensure_default_users(db)
    finally:
        db.close()
    # Precalentar índice de contenidos de _contexto_mpi/
    get_course_index()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url=None,      # Deshabilitar Swagger público en producción por seguridad
    redoc_url=None,
    openapi_url=None,
    lifespan=lifespan,
)

if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Authorization", "Content-Type"],
    )


@app.middleware("http")
async def security_headers_middleware(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    if request.url.path.startswith("/api/"):
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response


@app.get("/api/health")
def health():
    return {"status": "ok", "service": "mpi-pablo-platform", "version": settings.APP_VERSION}


app.include_router(auth_router.router)
app.include_router(content_router.router)
app.include_router(exercises_router.router)
app.include_router(exams_router.router)
app.include_router(security_router.router)
app.include_router(admin_router.router)

# Servir el frontend compilado (React + Vite) en producción / Docker
assets_dir = FRONTEND_DIST_DIR / "assets"
if assets_dir.exists():
    app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")


@app.get("/{full_path:path}")
def serve_spa(full_path: str):
    if full_path.startswith("api/"):
        return JSONResponse({"detail": "Endpoint no encontrado"}, status_code=404)
    candidate = FRONTEND_DIST_DIR / full_path
    if full_path and candidate.exists() and candidate.is_file():
        return FileResponse(str(candidate))
    index_html = FRONTEND_DIST_DIR / "index.html"
    if index_html.exists():
        return FileResponse(str(index_html))
    return JSONResponse(
        {
            "detail": "Frontend no compilado todavía. Ejecuta 'npm run build' dentro de frontend/.",
            "health": "/api/health",
        },
        status_code=503,
    )
