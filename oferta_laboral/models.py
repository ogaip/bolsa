from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField


ESTADO_CHOICES = {
    "Publicada": "Publicada",
    "No Publicada": "No Publicada",

}


# Create your models here.
class OfertaLaboral(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = HTMLField()
    habilidades_requeridas = HTMLField()
    requisitos_laborales = HTMLField()
    beneficios = HTMLField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_limite_postulacion = models.DateField()
    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default="Publicada")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
