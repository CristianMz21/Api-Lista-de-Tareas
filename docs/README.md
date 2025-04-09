# Documentación de la API de Lista de Tareas

## Índice
1. [Introducción](#introducción)
2. [Configuración del Proyecto](#configuración-del-proyecto)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Modelos](#modelos)
5. [API Endpoints](#api-endpoints)
6. [Pruebas](#pruebas)
7. [Despliegue](#despliegue)
8. [Contribución](#contribución)

## Introducción

Esta API permite gestionar una lista de tareas con las siguientes características:
- Autenticación de usuarios
- CRUD completo de tareas
- Priorización de tareas (Alta, Media, Baja)
- Marcado de tareas como completadas
- Interfaz de usuario responsiva
- API RESTful

## Configuración del Proyecto

### Requisitos
- Python 3.8+
- Django 4.0+
- PostgreSQL (para producción)
- SQLite (para desarrollo)

### Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/api-tareas.git
cd api-tareas
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:
```
DEBUG=True
SECRET_KEY=tu-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```

5. Ejecutar migraciones:
```bash
python manage.py migrate
```

6. Crear un superusuario:
```bash
python manage.py createsuperuser
```

7. Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

## Estructura del Proyecto

```
api-tareas/
├── api/                    # Configuración de la API para Vercel
├── ListaDeTareas/         # Configuración del proyecto Django
├── Tareas/                # Aplicación principal
│   ├── migrations/        # Migraciones de la base de datos
│   ├── static/           # Archivos estáticos
│   ├── templates/        # Plantillas HTML
│   ├── admin.py          # Configuración del admin
│   ├── forms.py          # Formularios
│   ├── models.py         # Modelos
│   ├── tests.py          # Pruebas
│   ├── urls.py           # URLs
│   └── views.py          # Vistas
├── docs/                  # Documentación
├── requirements.txt       # Dependencias
└── manage.py             # Script de gestión de Django
```

## Modelos

### Usuario
- `nombre`: Nombre del usuario
- `email`: Correo electrónico (único)
- `password`: Contraseña
- `fecha_registro`: Fecha de registro

### Tarea
- `titulo`: Título de la tarea
- `prioridad`: Prioridad (alta, media, baja)
- `descripcion`: Descripción detallada
- `fecha_creacion`: Fecha de creación
- `fecha_vencimiento`: Fecha límite (opcional)
- `completada`: Estado de completitud
- `usuario`: Usuario propietario

## API Endpoints

### Autenticación
- `POST /login/`: Iniciar sesión
- `POST /register/`: Registrar nuevo usuario
- `POST /logout/`: Cerrar sesión

### Tareas
- `GET /tareas/`: Listar todas las tareas del usuario
- `POST /tareas/`: Crear nueva tarea
- `GET /tareas/<id>/`: Obtener detalles de una tarea
- `PUT /tareas/<id>/`: Actualizar tarea
- `DELETE /tareas/<id>/`: Eliminar tarea
- `POST /tareas/<id>/toggle/`: Cambiar estado de completitud

### Ejemplos de Uso

#### Crear una nueva tarea
```python
import requests

url = "https://tu-api.com/tareas/"
headers = {
    "Authorization": "Token tu-token",
    "Content-Type": "application/json"
}
data = {
    "titulo": "Nueva tarea",
    "descripcion": "Descripción de la tarea",
    "prioridad": "alta",
    "fecha_vencimiento": "2024-12-31"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

#### Marcar tarea como completada
```python
import requests

url = "https://tu-api.com/tareas/1/toggle/"
headers = {
    "Authorization": "Token tu-token",
    "Content-Type": "application/json"
}
data = {
    "completada": True
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

## Pruebas

### Configuración de Pruebas

El proyecto incluye una configuración específica para pruebas en `ListaDeTareas/test_settings.py` que:
- Usa SQLite como base de datos para pruebas
- Deshabilita el hashing de contraseñas para pruebas más rápidas
- Deshabilita las migraciones durante las pruebas
- Configura un backend de correo en memoria
- Deshabilita el caché
- Configura archivos estáticos para pruebas

### Ejecución de Pruebas

Para ejecutar las pruebas, puedes usar:

1. El script personalizado:
```bash
python run_tests.py
```

2. O directamente con manage.py:
```bash
python manage.py test Tareas --settings=ListaDeTareas.test_settings
```

### Cobertura de Pruebas

Las pruebas cubren:
- Creación y validación de modelos
- Vistas y autenticación
- Operaciones CRUD
- Cambio de estado de tareas
- Manejo de errores
- Validación de datos

## Despliegue

### Despliegue en Vercel

1. Crear una cuenta en Vercel
2. Conectar con tu repositorio de GitHub
3. Configurar las variables de entorno en Vercel:
   - `DEBUG`: False
   - `SECRET_KEY`: Tu clave secreta
   - `DATABASE_URL`: URL de tu base de datos PostgreSQL
4. Desplegar

### Despliegue Local

1. Configurar PostgreSQL:
```bash
createdb api_tareas
```

2. Actualizar variables de entorno:
```
DEBUG=False
DATABASE_URL=postgres://usuario:contraseña@localhost:5432/api_tareas
```

3. Ejecutar migraciones:
```bash
python manage.py migrate
```

4. Recolectar archivos estáticos:
```bash
python manage.py collectstatic
```

5. Iniciar el servidor:
```bash
gunicorn ListaDeTareas.wsgi:application
```

## Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

### Guía de Estilo

- Seguir PEP 8 para Python
- Usar docstrings para documentar funciones y clases
- Escribir pruebas para nuevas funcionalidades
- Actualizar la documentación cuando sea necesario

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 