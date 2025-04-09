from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name=_("Nombre"))
    email = models.EmailField(unique=True, verbose_name=_("Correo Electrónico"))
    password = models.CharField(max_length=100, verbose_name=_("Contraseña"))
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de Registro"))

    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")
        ordering = ['-fecha_registro']

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    class Prioridad(models.TextChoices):
        ALTA = 'alta', _("Alta")
        MEDIA = 'media', _("Media")
        BAJA = 'baja', _("Baja")

    titulo = models.CharField(max_length=200, verbose_name=_("Título"))
    prioridad = models.CharField(
        max_length=10,
        choices=Prioridad.choices,
        default=Prioridad.MEDIA,
        verbose_name=_("Prioridad")
    )
    descripcion = models.TextField(verbose_name=_("Descripción"))
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de Creación"))
    fecha_vencimiento = models.DateTimeField(null=True, blank=True, verbose_name=_("Fecha de Vencimiento"))
    completada = models.BooleanField(default=False, verbose_name=_("Completada"))
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')

    class Meta:
        verbose_name = _("Tarea")
        verbose_name_plural = _("Tareas")
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo

    def clean(self):
        super().clean()
        if self.prioridad not in dict(self.Prioridad.choices):
            raise ValidationError({'prioridad': _('Prioridad inválida')})