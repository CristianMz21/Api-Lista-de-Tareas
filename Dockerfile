# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        postgresql-client \
        netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . .

# Hacer ejecutable el script de entrada
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Exponer el puerto
EXPOSE 8000

# Usar el script de entrada
ENTRYPOINT ["./entrypoint.sh"] 