#!/bin/sh

# Esperar a que la base de datos esté disponible
echo "Esperando a que la base de datos esté disponible..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Base de datos disponible"

# Aplicar migraciones
echo "Aplicando migraciones..."
python manage.py migrate

# Iniciar el servidor
echo "Iniciando servidor..."
python manage.py runserver 0.0.0.0:8000 