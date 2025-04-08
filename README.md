# Lista de Tareas - Aplicación Django

Una aplicación web de gestión de tareas construida con Django que permite a los usuarios crear, editar, eliminar y marcar tareas como completadas.

## Características

- Sistema de autenticación de usuarios (registro, inicio de sesión, cierre de sesión)
- Gestión completa de tareas (CRUD):
  - Crear nuevas tareas
  - Ver lista de tareas
  - Editar tareas existentes
  - Eliminar tareas
  - Marcar tareas como completadas
- Interfaz de usuario moderna y responsiva con Bootstrap 5
- Validación de formularios
- Mensajes de retroalimentación para las acciones del usuario
- Protección de rutas para usuarios no autenticados
- Cada usuario solo puede ver y gestionar sus propias tareas

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (recomendado)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/CristianMz21/Api-Lista-de-Tareas.git
cd Api-Lista-de-Tareas
```

2. Crear y activar un entorno virtual:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

4. Realizar las migraciones de la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crear un superusuario (opcional):
```bash
python manage.py createsuperuser
```

6. Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

La aplicación estará disponible en http://127.0.0.1:8000/tareas/

## Estructura del Proyecto

```
Api-Lista-de-Tareas/
├── ListaDeTareas/        # Configuración principal del proyecto
│   ├── settings.py       # Configuración de Django
│   └── urls.py          # URLs principales
├── Tareas/              # Aplicación de tareas
│   ├── models.py        # Modelos de datos
│   ├── views.py         # Vistas y lógica
│   ├── forms.py         # Formularios
│   ├── urls.py          # URLs de la aplicación
│   └── templates/       # Plantillas HTML
├── manage.py            # Script de gestión de Django
└── requirements.txt     # Dependencias del proyecto
```

## Uso

1. Registro de Usuario:
   - Accede a /tareas/register/
   - Completa el formulario con tu nombre de usuario, email y contraseña
   - Al registrarte exitosamente, serás redirigido a la lista de tareas

2. Inicio de Sesión:
   - Accede a /tareas/login/
   - Ingresa tu nombre de usuario y contraseña
   - Serás redirigido a tu lista de tareas

3. Gestión de Tareas:
   - Crear: Haz clic en el botón "Nueva Tarea"
   - Editar: Haz clic en el ícono de edición junto a la tarea
   - Eliminar: Haz clic en el ícono de papelera
   - Marcar como completada: Usa el checkbox junto a la tarea

4. Cierre de Sesión:
   - Haz clic en "Cerrar Sesión" en la barra de navegación

## Características de las Tareas

Cada tarea incluye:
- Título (obligatorio)
- Descripción (opcional)
- Prioridad
- Fecha de vencimiento
- Estado de completado
- Fecha de creación (automática)
- Usuario asignado (automático)

## Seguridad

- Todas las rutas están protegidas y requieren autenticación
- Los usuarios solo pueden ver y modificar sus propias tareas
- Protección CSRF en todos los formularios
- Validación de datos en el servidor
- Contraseñas hasheadas y seguras

## Contribuir

1. Haz un Fork del proyecto
2. Crea una rama para tu función (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 