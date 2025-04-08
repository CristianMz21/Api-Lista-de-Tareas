from django.contrib import admin
from .models import Usuario, Tarea

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha_registro')
    search_fields = ('nombre', 'email')
    list_filter = ('fecha_registro',)
    ordering = ('-fecha_registro',)

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'prioridad', 'fecha_creacion', 'fecha_vencimiento', 'completada')
    list_filter = ('prioridad', 'completada', 'fecha_creacion', 'fecha_vencimiento')
    search_fields = ('titulo', 'descripcion', 'usuario__username')
    list_editable = ('completada',)
    ordering = ('-fecha_creacion',)
