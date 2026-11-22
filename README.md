# MPI-I · Plataforma Blindada de Estudio, Entrenamiento y Evaluación (UFV)

Plataforma web full-stack de alto rendimiento diseñada para el seguimiento intensivo de **Matemáticas para la Ingeniería I (código 5666 · Grado en Ingeniería Informática · UFV)**, construida íntegramente a partir de los materiales académicos indexados en [`_contexto_mpi/`](_contexto_mpi/).

## Arquitectura Técnica

| Capa | Tecnología | Propósito |
|---|---|---|
| **Backend API** | Python 3.12 + FastAPI + Pydantic v2 | Autenticación dual, bloqueo estricto de soluciones en servidor, auditoría y analítica |
| **Motor Matemático** | SymPy + NumPy | 26 generadores procedurales exactos con aritmética racional limpia, verificación simbólica y análisis real de la Red Logística LOGISPAÑA |
| **Persistencia** | SQLite (modo WAL) + SQLAlchemy 2.0 | Un único fichero `data/mpi_platform.db` para backups instantáneos en VPS |
| **Frontend SPA** | React 19 + TypeScript + Vite + Vanilla CSS | Interfaz oscura tipo IDE/Linear, **KaTeX** y **Highlight.js** empaquetados localmente (sin dependencia de CDNs externos) |
| **Despliegue** | Docker multi-stage + Docker Compose + Nginx | Despliegue en un solo comando en VPS Ubuntu/Debian detrás de HTTPS |

## Módulos Principales

1. **Teoría Interactiva (`_contexto_mpi/00..05`):**
   - Guía docente UFV, tabla de secciones del Grossman 8.ª ed. y **Checklist interactivo** («Qué hay que saber de Álgebra») persistido por usuario.
   - 4 bloques estructurados (Sistemas/Matrices/Determinantes, Espacios Vectoriales, Aplicaciones Lineales, Autovalores y Diagonalización) con definiciones, teoremas clave, ejemplos resueltos paso a paso, pizarras de clase y **bloc de notas rápido integrado con vista KaTeX**.
   - Buscador instantáneo de teoremas, definiciones, funciones MATLAB y retos del proyecto.
2. **Motor de Ejercicios Infinitos (Procedural / Paramétrico):**
   - **26 generadores algorítmicos** cubriendo todos los tipos de problema de los boletines (`05`), exámenes CO/CEX (`07`, `08`), banco de 122 preguntas (`09`) y prácticas MATLAB (`06`).
   - Matrices unimodulares ($\det = \pm 1$) y aritmética racional SymPy para garantizar resultados limpios (enteros o fracciones manejables).
   - **Deduplicación por huella criptográfica** en SQLite: Pablo nunca repite el mismo ejercicio dos veces.
   - **Bloqueo estricto de respuestas:** el servidor jamás envía la solución ni los pasos al frontend hasta la entrega o expiración del temporizador.
3. **Sistema Anti-IA y Anti-Trampas (Lockdown Mode):**
   - Modal de onboarding obligatorio con aceptación de reglas antes de iniciar cualquier bloque o simulacro.
   - **Pantalla Completa obligatoria** (`Fullscreen API`).
   - Detección inmediata de salida de pantalla completa, cambio de pestaña (`visibilitychange`), pérdida de foco (`blur` / Alt+Tab) e intentos de DevTools (`F12` / `Ctrl+Shift+I`), con **alerta sonora (Web Audio API)**, bloqueo visual, registro en SQLite, invalidación en servidor y reinicio con problemas totalmente nuevos.
   - Bloqueo de selección (`user-select: none`), clic derecho y portapapeles (`Ctrl+C/V/X`).
   - **Renderizado Anti-OCR:** marca de agua dinámica en `<canvas>` con nombre y reloj en vivo + matrices críticas renderizadas directamente en `<canvas>` protegido.
   - **Pizarra Digital (Canvas) + Bloc de cálculos en sucio** integrado en pantalla para no abandonar jamás la ventana.
4. **Simulador de Exámenes UFV y Banco Histórico:**
   - Modalidades **Ordinaria (90 min, 9 preguntas)**, **Extraordinaria (105 min, 9 preguntas)** y **Express (35 min, 5 bloques)** generadas 100% proceduralmente en cada intento.
   - Índice completo de las **122 preguntas del banco histórico (2022–2026)** y los **38 enunciados prácticos MATLAB**.
5. **Laboratorio MATLAB y Proyecto 01 · Red Logística (LOGISPAÑA):**
   - Chuleta interactiva de funciones, rúbrica oficial `Formato_practicas_Matlab_2026`, los 8 bloques del cuaderno común y prácticas evaluables 1–3 con resaltado MATLAB.
   - **Simulador interactivo real (NumPy)** de la red logística de 12 centros y 22 rutas (`P01 Datos.xlsx`), ajuste polinomial 2028, 3 métodos Markov con residuo $< 10^{-12}$, ranking multicriterio y simulación **DANA en Valencia** + entrenador de Defensa Oral (70%).
6. **Panel de Control del Profesor (`/admin`):**
   - Estado en tiempo real de Pablo, sesiones con IP real y dispositivo, contador de accesos, tiempo efectivo real (descontando inactividad mediante heartbeats), racha de días, log completo de infracciones anti-trampas, precisión y tiempo medio por tema, detector automático de puntos débiles y **exportación en CSV y JSON**.

> **Nota RGPD / Privacidad:** El archivo `_contexto_mpi/11_Administrativo_listados_y_aulas.md` contiene datos personales de terceros estudiantes y queda deliberadamente excluido de la indexación de la aplicación.

---

## Despliegue Rápido en VPS (1 comando)

Consulta la guía completa en [`DEPLOY_VPS.md`](DEPLOY_VPS.md):

```bash
cp .env.example .env
# Edita .env con SECRET_KEY y contraseñas seguras
mkdir -p data
docker compose up -d --build
```

## Desarrollo Local y Pruebas

```bash
# 1. Instalar dependencias Python y lanzar tests (motor matemático + seguridad + RBAC)
pip install -r backend/requirements.txt pytest httpx
PYTHONPATH=. pytest -v backend/tests/

# 2. Compilar el frontend
cd frontend && npm install && npm run build && cd ..

# 3. Arrancar servidor unificado (API + Frontend)
uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```
