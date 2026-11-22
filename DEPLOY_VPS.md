# Guía de Despliegue en VPS Personal (Ubuntu / Debian) con Docker + Nginx + HTTPS

Esta guía te permite poner en marcha la plataforma **MPI-I · Entorno Blindado para Pablo** en tu VPS en menos de 5 minutos.

---

## 1. Requisitos previos en el VPS

```bash
sudo apt-get update
sudo apt-get install -y git curl nginx certbot python3-certbot-nginx sqlite3
```

Si aún no tienes Docker y el plugin Compose instalados:

```bash
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER
# Cierra sesión SSH y vuelve a entrar para aplicar el grupo docker
```

---

## 2. Clonar el repositorio y configurar credenciales (`.env`)

```bash
git clone https://github.com/alfonsodfernandez/mpi.git /opt/mpi-pablo
cd /opt/mpi-pablo
cp .env.example .env
```

Genera una clave criptográfica aleatoria y edita `.env` con tus contraseñas seguras:

```bash
openssl rand -hex 32
nano .env
```

Asegúrate de configurar:
- `SECRET_KEY`: pega el valor generado con `openssl rand -hex 32`.
- `PABLO_USERNAME` y `PABLO_PASSWORD`: credenciales exclusivas de Pablo.
- `ADMIN_USERNAME` y `ADMIN_PASSWORD`: tus credenciales privadas para `/admin`.
- `COOKIE_SECURE=true` (cuando uses HTTPS con Nginx; usa `false` únicamente si pruebas en HTTP local sin TLS).

Prepara la carpeta persistente de SQLite con permisos para el usuario del contenedor:

```bash
mkdir -p data
chmod 775 data
```

---

## 3. Levantar la plataforma con un solo comando

```bash
docker compose up -d --build
```

Comprueba que el servicio responde correctamente en `localhost`:

```bash
docker compose ps
curl -s http://127.0.0.1:8000/api/health
# Salida esperada: {"status":"ok","service":"mpi-pablo-platform","version":"1.0.0"}
```

---

## 4. Configurar Nginx + Certificado HTTPS (Let's Encrypt)

1. Crea un registro DNS `A` apuntando tu dominio/subdominio (ej. `mpi.tudominio.com`) a la IP pública de tu VPS.
2. Copia la plantilla de Nginx y reemplaza `mpi.tudominio.com`:

```bash
sudo cp nginx/mpi-pablo.conf /etc/nginx/sites-available/mpi-pablo.conf
sudo sed -i 's/mpi.tudominio.com/TU_DOMINIO_REAL/g' /etc/nginx/sites-available/mpi-pablo.conf
```

3. Emite el certificado TLS gratuito con Certbot (primero en modo standalone o temporalmente comentando las líneas `ssl_certificate` si el certificado aún no existe):

```bash
sudo certbot certonly --nginx -d TU_DOMINIO_REAL
```

4. Activa el sitio y recarga Nginx:

```bash
sudo ln -sf /etc/nginx/sites-available/mpi-pablo.conf /etc/nginx/sites-enabled/mpi-pablo.conf
sudo nginx -t && sudo systemctl reload nginx
```

5. Configura el cortafuegos UFW (dejando solo SSH, HTTP y HTTPS; el puerto `8000` ya está restringido a `127.0.0.1`):

```bash
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

---

## 5. Backups automáticos diarios de SQLite

Al usar SQLite en modo WAL (`./data/mpi_platform.db`), puedes realizar copias en caliente sin detener el contenedor usando `.backup`:

```bash
mkdir -p /opt/backups-mpi
(crontab -l 2>/dev/null; echo "0 3 * * * sqlite3 /opt/mpi-pablo/data/mpi_platform.db \".backup '/opt/backups-mpi/mpi_\$(date +\%F).db'\" && find /opt/backups-mpi -name 'mpi_*.db' -mtime +30 -delete") | crontab -
```

---

## 6. Actualización y Mantenimiento

```bash
cd /opt/mpi-pablo
git pull
docker compose up -d --build
docker compose logs -f --tail=50
```

### Rutas de acceso
- **Alumno (Pablo):** `https://TU_DOMINIO_REAL/`
- **Profesor (Auditoría y Analítica):** `https://TU_DOMINIO_REAL/admin`
