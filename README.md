# API de Lista de Tareas

Esta es una API RESTful para gestionar una lista de tareas, desarrollada con Django y desplegada en Vercel.

## Características

- Autenticación de usuarios
- CRUD completo de tareas
- Priorización de tareas (Alta, Media, Baja)
- Marcado de tareas como completadas
- Interfaz de usuario responsiva
- API RESTful

## Requisitos

- Python 3.8+
- Django 4.0+
- PostgreSQL (para producción)
- SQLite (para desarrollo)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/CristianMz21/Api-Lista-de-Tareas.git
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

## Endpoints de la API

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

## Ejemplos de Uso

### Crear una nueva tarea
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

### Marcar tarea como completada
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

Para ejecutar las pruebas:
```bash
python manage.py test Tareas
```

Las pruebas cubren:
- Creación y validación de modelos
- Vistas y autenticación
- Operaciones CRUD
- Cambio de estado de tareas

## Despliegue

El proyecto está configurado para desplegarse en Vercel. Para desplegar:

1. Crear una cuenta en Vercel
2. Conectar con tu repositorio de GitHub
3. Configurar las variables de entorno en Vercel
4. Desplegar

## Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
