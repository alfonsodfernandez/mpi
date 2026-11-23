# ==============================================================================
# Stage 1: Build Frontend (React + Vite + KaTeX + Highlight.js self-contained)
# ==============================================================================
FROM node:22-alpine AS frontend-builder

WORKDIR /build/frontend
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm install --no-audit --no-fund
COPY frontend/ ./
RUN npm run build

# ==============================================================================
# Stage 2: Production Backend (Python 3.12 + FastAPI + SymPy + NumPy + SQLite)
# ==============================================================================
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    CONTEXT_DIR=/app/_contexto_mpi \
    FRONTEND_DIST_DIR=/app/frontend/dist \
    DATA_DIR=/app/data \
    DATABASE_URL=sqlite:////app/data/mpi_platform.db

WORKDIR /app

# Dependencias mínimas del sistema (curl para healthcheck y sqlite3 para backups)
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl sqlite3 && \
    rm -rf /var/lib/apt/lists/*

# Instalar dependencias Python
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --upgrade pip && pip install -r ./backend/requirements.txt

# Copiar contexto académico del curso, código backend y bundle frontend compilado
COPY _contexto_mpi/ ./_contexto_mpi/
COPY backend/ ./backend/
COPY --from=frontend-builder /build/frontend/dist ./frontend/dist

# Crear directorio de datos persistentes y usuario sin privilegios (UID/GID 1000 por defecto, compatible con host Ubuntu/Debian)
ARG APP_UID=1000
ARG APP_GID=1000
RUN mkdir -p /app/data && \
    groupadd -g ${APP_GID} appuser && \
    useradd -u ${APP_UID} -g ${APP_GID} -d /app -s /usr/sbin/nologin appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD curl -fsS http://127.0.0.1:8000/api/health || exit 1

# Un solo worker mantiene SQLite WAL ultrarrápido y rate-limiter coherente para uso personal (Pablo + Profesor)
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--forwarded-allow-ips=*"]
