from .settings import *
import os

# Configuración de la base de datos para pruebas
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
    }
}

# Deshabilitar el hashing de contraseñas para pruebas más rápidas
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Deshabilitar migraciones durante las pruebas
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

# Configuración de correo para pruebas
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Deshabilitar el caché para pruebas
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Configuración de archivos estáticos para pruebas
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Deshabilitar la validación de plantillas durante las pruebas
TEMPLATES[0]['OPTIONS']['debug'] = False

# Deshabilitar la recolección de archivos estáticos durante las pruebas
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
] 