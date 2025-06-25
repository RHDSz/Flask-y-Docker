# 🐳 Aplicación Flask en Docker

🔹 **Versión:** 1.0  
🔹 **Autor:** [Tu Nombre]  
🔹 **Repositorio:** [Enlace a GitHub]

---

## 📌 Descripción del Proyecto

Este proyecto implementa una aplicación web Flask que detecta y muestra la dirección IP del cliente en diferentes versiones (puertos 8000, 8181 y 8888), cada una con mejoras progresivas. La aplicación se ejecuta dentro de un contenedor Docker para facilitar su despliegue y portabilidad.

---

## 🚀 Características Principales

✅ 3 versiones de la aplicación (básica, con HTML y Dockerizada)  
✅ Detección automática de IP del cliente  
✅ Plantilla HTML para una mejor visualización  
✅ Configuración optimizada para Docker  
✅ Fácil despliegue con un solo comando

---

## ⚙️ Requisitos Previos

### 📦 Dependencias (Python)

| Librería   | Versión | Descripción                          |
|------------|---------|--------------------------------------|
| Flask      | 2.0+    | Framework web para Python            |


# Dependencias (Docker)

- Docker Engine 20.10+  
- Docker Compose (opcional)

---

## 📂 Estructura del Proyecto

```
flask-ip-docker/
sample_app.py          # Código principal (modificado en cada paso)
Dockerfile             # Configuración para Docker
requirements.txt       # Dependencias de Python
static/                # CSS/JS (opcional)
templates/             # Plantillas HTML
index.html         # Página para mostrar la IP
```

---

## 🚀 Instalación y Uso

### 1️⃣ Paso 1: Versión Básica (Puerto 8000)

**`sample_app.py`**

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    return "Tu dirección IP es: " + request.remote_addr + "\n"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
```

▶️ **Ejecución:**

```bash
python3 sample_app.py
```

🔹 Acceso: [http://localhost:8000](http://localhost:8000)

---

### 2️⃣ Paso 2: Versión con HTML (Puerto 8181)

**`sample_app.py`**

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html", ip_address=request.remote_addr)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8181)
```

**`templates/index.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Detector de IP</title>
</head>
<body>
    <h1>Tu dirección IP es: {{ ip_address }}</h1>
</body>
</html>
```

▶️ **Ejecución:**

```bash
python3 sample_app.py
```

🔹 Acceso: [http://localhost:8181](http://localhost:8181)

---

### 3️⃣ Paso 3: Versión Dockerizada (Puerto 8888)

**`sample_app.py`**

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    ip_cliente = request.remote_addr
    return f"La conexión se está realizando desde: {ip_cliente}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
```

**`Dockerfile`**

```dockerfile
FROM python:3.10-slim

ENV PIP_NO_PROGRESS_BAR=off

RUN pip install --no-cache-dir flask

COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY sample_app.py /home/myapp/

EXPOSE 8888

CMD ["python3", "/home/myapp/sample_app.py"]
```

▶️ **Construcción y ejecución:**

```bash
docker build -t flask-ip-app .
docker run -p 8888:8888 flask-ip-app
```

🔹 Acceso: [http://localhost:8888](http://localhost:8888)

---

## 📌 Comandos Útiles

| Comando                   | Descripción                       |
|--------------------------|-----------------------------------|
| `docker ps`              | Ver contenedores en ejecución     |
| `docker stop <ID>`       | Detener un contenedor             |
| `docker rm <ID>`         | Eliminar un contenedor            |
| `docker rmi flask-ip-app`| Eliminar la imagen creada         |

---

## 📜 Licencia

Este proyecto está bajo la licencia **MIT**.

---

## 📧 Contacto

✉️ Correo: [fcer14.2002@gmail.com]
