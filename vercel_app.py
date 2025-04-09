from django.core.wsgi import get_wsgi_application
import os
import sys
import django
from django.db import connections
from django.db.utils import OperationalError

# Asegurar que el directorio raíz del proyecto esté en el path
sys.path.append(os.getcwd())

# Configurar el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ListaDeTareas.settings')

# Marcar que estamos en Vercel
os.environ['VERCEL'] = 'True'

# Inicializar Django
django.setup()

# Ejecutar migraciones automáticamente y crear superusuario
try:
    from django.core.management import call_command
    # Ejecutar migraciones
    call_command('migrate', '--noinput')
    
    # Crear superusuario si no existe
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin1234'
        )
    print("Migraciones y creación de usuario completadas con éxito")
except Exception as e:
    print(f"Error al ejecutar migraciones: {e}")

# Iniciar la aplicación Django después de las migraciones
app = get_wsgi_application() 