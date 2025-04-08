# API de Autenticación de Usuarios con FastAPI

Esta es una API para gestión de usuarios con sistema de autenticación implementada con FastAPI. Permite el registro de usuarios, inicio de sesión, y gestión de usuarios con autenticación JWT.

## Características

- Registro de usuarios
- Autenticación con JWT
- Protección de rutas con OAuth2
- Gestión de usuarios (listar, obtener por ID)
- Encriptación de contraseñas con bcrypt
- Base de datos SQLite con SQLAlchemy ORM

## Requisitos

- Python 3.13.2
- Dependencias listadas en `requirements.txt` (todas actualizadas para compatibilidad con Python 3.13.2)

## Instalación

1. Clonar el repositorio

2. Crear un entorno virtual (opcional pero recomendado)
   ```
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   ```

3. Instalar dependencias
   ```
   pip install -r requirements.txt
   ```

4. Ejecutar la aplicación
   ```
   uvicorn main:app --reload
   ```

5. Acceder a la documentación de la API en `http://localhost:8000/docs`

## Estructura del Proyecto

- `main.py`: Punto de entrada de la aplicación
- `auth.py`: Rutas de autenticación (registro, login)
- `models.py`: Modelos de datos y esquemas Pydantic
- `security.py`: Funciones de seguridad (hash, JWT, OAuth2)
- `database.py`: Configuración de la base de datos
- `config.py`: Configuración de la aplicación

## Endpoints

### Autenticación

- `POST /auth/register`: Registrar un nuevo usuario
- `POST /auth/token`: Iniciar sesión y obtener token JWT
- `GET /auth/users/me`: Obtener información del usuario actual

### Usuarios (requieren autenticación)

- `GET /users/`: Listar todos los usuarios
- `GET /users/{user_id}`: Obtener usuario por ID

## Ejemplo de Uso

### Registrar un usuario

```bash
curl -X 'POST' \
  'http://localhost:8000/auth/register' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "usuario@ejemplo.com",
  "username": "usuario",
  "password": "contraseña123"
}'
```

### Iniciar sesión

```bash
curl -X 'POST' \
  'http://localhost:8000/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=usuario&password=contraseña123'
```

### Acceder a un endpoint protegido

```bash
curl -X 'GET' \
  'http://localhost:8000/users/' \
  -H 'Authorization: Bearer {tu_token_jwt}'
```