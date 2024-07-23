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
    fecha_limite_postulacion = models.DateField(blank=False, null=False)
    estado = models.CharField(
        choices=ESTADO_CHOICES,
        default="Publicada"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = "Oferta Laboral"
        verbose_name_plural = "Ofertas Laborales"
        db_table = "OfertasLaborales"

    def __str__(self):
        return self.titulo
