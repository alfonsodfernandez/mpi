"""Autenticación dual (Alumno / Profesor), scrypt hashing, tokens firmados y auditoría de IP/dispositivo."""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import secrets
import time
import uuid
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi import Depends, HTTPException, Request, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .config import settings
from .database import get_db
from .models import StudySession, User, utcnow

COOKIE_NAME = "mpi_session_token"

# Rate-limiting en memoria para evitar fuerza bruta en /api/auth/login
_LOGIN_ATTEMPTS: dict[str, list[float]] = defaultdict(list)
MAX_LOGIN_ATTEMPTS = 15
LOGIN_WINDOW_SECONDS = 300


def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)
    dk = hashlib.scrypt(password.encode("utf-8"), salt=salt, n=2**14, r=8, p=1, dklen=32)
    return f"scrypt$16384$8$1${base64.b64encode(salt).decode()}${base64.b64encode(dk).decode()}"


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        scheme, n_s, r_s, p_s, salt_b64, dk_b64 = stored_hash.split("$")
        if scheme != "scrypt":
            return False
        salt = base64.b64decode(salt_b64)
        expected = base64.b64decode(dk_b64)
        derived = hashlib.scrypt(
            password.encode("utf-8"),
            salt=salt,
            n=int(n_s),
            r=int(r_s),
            p=int(p_s),
            dklen=len(expected),
        )
        return hmac.compare_digest(derived, expected)
    except Exception:
        return False


def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _b64url_decode(s: str) -> bytes:
    pad = "=" * ((4 - len(s) % 4) % 4)
    return base64.urlsafe_b64decode(s + pad)


def create_access_token(user_id: int, username: str, role: str, session_id: str) -> str:
    header = _b64url_encode(json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":")).encode())
    exp = int((datetime.now(timezone.utc) + timedelta(hours=settings.SESSION_EXPIRE_HOURS)).timestamp())
    payload_dict = {
        "sub": user_id,
        "usr": username,
        "role": role,
        "sid": session_id,
        "iat": int(time.time()),
        "exp": exp,
    }
    payload = _b64url_encode(json.dumps(payload_dict, separators=(",", ":")).encode())
    signing_input = f"{header}.{payload}".encode("ascii")
    sig = hmac.new(settings.SECRET_KEY.encode("utf-8"), signing_input, hashlib.sha256).digest()
    return f"{header}.{payload}.{_b64url_encode(sig)}"


def decode_access_token(token: str) -> dict[str, Any]:
    try:
        parts = token.split(".")
        if len(parts) != 3:
            raise ValueError("Malformed token")
        header_b64, payload_b64, sig_b64 = parts
        signing_input = f"{header_b64}.{payload_b64}".encode("ascii")
        expected_sig = hmac.new(settings.SECRET_KEY.encode("utf-8"), signing_input, hashlib.sha256).digest()
        provided_sig = _b64url_decode(sig_b64)
        if not hmac.compare_digest(expected_sig, provided_sig):
            raise ValueError("Invalid signature")
        payload = json.loads(_b64url_decode(payload_b64).decode("utf-8"))
        if payload.get("exp", 0) < int(time.time()):
            raise ValueError("Token expired")
        return payload
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sesión no válida o expirada. Inicia sesión nuevamente.",
        ) from exc


def extract_client_ip(request: Request) -> str:
    if settings.TRUST_PROXY_HEADERS:
        forwarded = request.headers.get("x-forwarded-for")
        if forwarded:
            return forwarded.split(",")[0].strip()[:64]
        real_ip = request.headers.get("x-real-ip")
        if real_ip:
            return real_ip.strip()[:64]
    if request.client and request.client.host:
        return request.client.host[:64]
    return "unknown"


def summarize_user_agent(ua: str) -> str:
    ua_l = (ua or "").lower()
    if not ua_l:
        return "Navegador desconocido"

    if "edg/" in ua_l:
        browser = "Edge"
    elif "opr/" in ua_l or "opera" in ua_l:
        browser = "Opera"
    elif "firefox/" in ua_l:
        browser = "Firefox"
    elif "chrome/" in ua_l and "chromium" not in ua_l:
        browser = "Chrome"
    elif "safari/" in ua_l:
        browser = "Safari"
    else:
        browser = "Otro navegador"

    if "windows" in ua_l:
        os_name = "Windows"
    elif "mac os" in ua_l or "macintosh" in ua_l:
        os_name = "macOS"
    elif "ipad" in ua_l or "iphone" in ua_l:
        os_name = "iOS"
    elif "android" in ua_l:
        os_name = "Android"
    elif "linux" in ua_l:
        os_name = "Linux"
    else:
        os_name = "SO desconocido"

    return f"{browser} en {os_name}"


def check_login_rate_limit(ip: str) -> None:
    now = time.time()
    recent = [ts for ts in _LOGIN_ATTEMPTS[ip] if now - ts < LOGIN_WINDOW_SECONDS]
    _LOGIN_ATTEMPTS[ip] = recent
    if len(recent) >= MAX_LOGIN_ATTEMPTS:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Demasiados intentos de acceso. Espera unos minutos.",
        )


def record_failed_login(ip: str) -> None:
    _LOGIN_ATTEMPTS[ip].append(time.time())


def ensure_default_users(db: Session) -> None:
    """Crea o sincroniza los dos usuarios exclusivos (Pablo y Profesor) desde variables de entorno."""
    desired = [
        (settings.PABLO_USERNAME, settings.PABLO_DISPLAY_NAME, "student", settings.PABLO_PASSWORD),
        (settings.ADMIN_USERNAME, settings.ADMIN_DISPLAY_NAME, "admin", settings.ADMIN_PASSWORD),
    ]
    for username, display_name, role, raw_password in desired:
        user = db.execute(select(User).where(User.username == username)).scalar_one_or_none()
        if user is None:
            user = User(
                username=username,
                display_name=display_name,
                role=role,
                password_hash=hash_password(raw_password),
            )
            db.add(user)
        else:
            user.display_name = display_name
            user.role = role
            if not verify_password(raw_password, user.password_hash):
                user.password_hash = hash_password(raw_password)
    db.commit()


def create_study_session(db: Session, user: User, request: Request) -> StudySession:
    ua = request.headers.get("user-agent", "")[:512]
    sess = StudySession(
        id=str(uuid.uuid4()),
        user_id=user.id,
        started_at=utcnow(),
        last_seen_at=utcnow(),
        ip_address=extract_client_ip(request),
        user_agent=ua,
        device_summary=summarize_user_agent(ua),
        is_active=True,
    )
    user.last_login_at = utcnow()
    db.add(sess)
    db.commit()
    db.refresh(sess)
    return sess


class AuthContext:
    def __init__(self, user: User, session_id: str):
        self.user = user
        self.session_id = session_id


def _extract_token(request: Request) -> str:
    auth_header = request.headers.get("authorization", "")
    if auth_header.lower().startswith("bearer "):
        return auth_header[7:].strip()
    cookie_token = request.cookies.get(COOKIE_NAME)
    if cookie_token:
        return cookie_token
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Autenticación requerida.",
    )


def get_current_auth(request: Request, db: Session = Depends(get_db)) -> AuthContext:
    token = _extract_token(request)
    payload = decode_access_token(token)
    user_id = payload.get("sub")
    session_id = payload.get("sid", "")
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado.")
    sess = db.get(StudySession, session_id)
    if sess is None or not sess.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sesión cerrada o expirada.")
    return AuthContext(user=user, session_id=session_id)


def require_admin(ctx: AuthContext = Depends(get_current_auth)) -> AuthContext:
    if ctx.user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acceso restringido exclusivamente al profesor (/admin).",
        )
    return ctx
