from django.db import models
from django_prose_editor.sanitized import SanitizedProseEditorField
from django_prose_editor.fields import ProseEditorField, ProseEditorWidget, ProseEditorFormField
from django.contrib.auth.models import User


ESTADO_CHOICES = {
    "Publicada": "Publicada",
    "No Publicada": "No Publicada",

}



# Create your models here.
class OfertaLaboral(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = ProseEditorField(max_length=200)
    habilidades_requeridas = ProseEditorField()
    requisitos_laborales = SanitizedProseEditorField()
    beneficios = SanitizedProseEditorField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_limite_postulacion = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES ,default="Publicada")
    empleador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
