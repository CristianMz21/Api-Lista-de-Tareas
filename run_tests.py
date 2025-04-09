import os
import sys
import subprocess
from django.core.management import execute_from_command_line

def run_tests():
    # Crear directorio de archivos estáticos si no existe
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'staticfiles')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    # Ejecutar las pruebas
    execute_from_command_line(['manage.py', 'test', 'Tareas', '--settings=ListaDeTareas.test_settings'])

if __name__ == '__main__':
    run_tests() 