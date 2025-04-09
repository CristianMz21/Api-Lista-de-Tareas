# Guía de Pruebas

## Índice
1. [Introducción](#introducción)
2. [Configuración de Pruebas](#configuración-de-pruebas)
3. [Ejecución de Pruebas](#ejecución-de-pruebas)
4. [Cobertura de Pruebas](#cobertura-de-pruebas)
5. [Mejores Prácticas](#mejores-prácticas)

## Introducción

Este documento describe cómo ejecutar y escribir pruebas para la API de Lista de Tareas. El proyecto utiliza el framework de pruebas de Django y sigue las mejores prácticas de desarrollo guiado por pruebas (TDD).

## Configuración de Pruebas

### Base de Datos de Pruebas

El proyecto utiliza SQLite para las pruebas, configurado en `ListaDeTareas/test_settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
    }
}
```

### Configuración Adicional

- Deshabilitación de hashing de contraseñas para pruebas más rápidas
- Deshabilitación de migraciones durante las pruebas
- Configuración de backend de correo en memoria
- Deshabilitación de caché
- Configuración de archivos estáticos para pruebas

## Ejecución de Pruebas

### Opción 1: Usando el Script Personalizado

```bash
python run_tests.py
```

Este script:
1. Crea el directorio de archivos estáticos si no existe
2. Ejecuta las pruebas con la configuración correcta

### Opción 2: Usando manage.py

```bash
python manage.py test Tareas --settings=ListaDeTareas.test_settings
```

### Opciones Adicionales

- Ejecutar pruebas específicas:
```bash
python manage.py test Tareas.tests.TareaModelTest
```

- Ejecutar con verbosidad aumentada:
```bash
python manage.py test Tareas -v 2
```

- Ejecutar con cobertura:
```bash
coverage run --source='.' manage.py test Tareas
coverage report
```

## Cobertura de Pruebas

### Modelos

Las pruebas de modelos cubren:
- Creación de instancias
- Validación de campos
- Relaciones entre modelos
- Métodos personalizados
- Elecciones de campos (choices)

### Vistas

Las pruebas de vistas cubren:
- Autenticación y autorización
- Respuestas HTTP correctas
- Redirecciones
- Manejo de formularios
- Respuestas JSON
- Manejo de errores

### API

Las pruebas de API cubren:
- Endpoints REST
- Autenticación de tokens
- Validación de datos
- Respuestas de error
- Estados de tareas

## Mejores Prácticas

### Escribiendo Pruebas

1. **Nombres Descriptivos**
```python
def test_tarea_creation_with_invalid_priority(self):
    # ...
```

2. **Documentación Clara**
```python
def test_toggle_completada_view(self):
    """Test toggling tarea completion status with valid JSON"""
    # ...
```

3. **Setup y Teardown**
```python
def setUp(self):
    self.client = Client()
    self.user = User.objects.create_user(...)
```

4. **Aserciones Específicas**
```python
self.assertEqual(response.status_code, 200)
self.assertContains(response, 'Test Tarea')
```

### Mantenimiento de Pruebas

1. **Pruebas Independientes**
- Cada prueba debe ser independiente
- No depender del estado de otras pruebas
- Limpiar el estado después de cada prueba

2. **Pruebas Rápidas**
- Usar SQLite para pruebas
- Deshabilitar funcionalidades innecesarias
- Minimizar el uso de la base de datos

3. **Pruebas Significativas**
- Probar casos de éxito y error
- Probar casos límite
- Probar validaciones

### Depuración de Pruebas

1. **Usar Verbosidad**
```bash
python manage.py test Tareas -v 2
```

2. **Pruebas Individuales**
```bash
python manage.py test Tareas.tests.TareaViewTest.test_tarea_create_view
```

3. **Usar pdb**
```python
import pdb; pdb.set_trace()
```

## Ejemplos de Pruebas

### Prueba de Modelo
```python
def test_tarea_creation(self):
    """Test that a tarea can be created"""
    tarea = Tarea.objects.create(
        titulo='Test Tarea',
        descripcion='Test Descripción',
        usuario=self.user
    )
    self.assertEqual(tarea.titulo, 'Test Tarea')
    self.assertEqual(tarea.prioridad, 'media')
```

### Prueba de Vista
```python
def test_tarea_create_view(self):
    """Test tarea creation"""
    self.client.login(username='testuser', password='testpass123')
    response = self.client.post(self.tarea_create_url, {
        'titulo': 'Nueva Tarea',
        'descripcion': 'Nueva Descripción',
        'prioridad': 'alta'
    })
    self.assertEqual(response.status_code, 302)
    self.assertTrue(Tarea.objects.filter(titulo='Nueva Tarea').exists())
```

### Prueba de API
```python
def test_toggle_completada_view(self):
    """Test toggling tarea completion status"""
    self.client.login(username='testuser', password='testpass123')
    response = self.client.post(
        self.toggle_completada_url,
        json.dumps({'completada': True}),
        content_type='application/json'
    )
    self.assertEqual(response.status_code, 200)
    self.tarea.refresh_from_db()
    self.assertTrue(self.tarea.completada)
``` 