from django.db import models

# Create your models here.

from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

User = get_user_model()

ESTADO_CHOICES = {
    "Publicada": "Publicada",
    "No Publicada": "No Publicada",
}


# Create your models here.
class OfertaLaboral(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    titulo = models.CharField(max_length=200)
    descripcion = HTMLField()
    habilidades_requeridas = HTMLField()
    requisitos_laborales = HTMLField()
    beneficios = HTMLField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_limite_postulacion = models.DateField(blank=False, null=False)
    estado = models.CharField(choices=ESTADO_CHOICES, default="Publicada")

    class Meta:
        verbose_name = "Oferta Laboral"
        verbose_name_plural = "Ofertas Laborales"
        db_table = "OfertasLaborales"

    def __str__(self):
        return self.titulo

    def views_count(self):
        return self.views.count()

    def like_count(self):
        return self.like.count()


class View(models.Model):
    oferta = models.ForeignKey(
        OfertaLaboral, related_name="views", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} vio {self.OfertaLaboral.titulo}"


class Like(models.Model):
    oferta = models.ForeignKey(
        OfertaLaboral, related_name="likes", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        db_table = "Likes"
        unique_together = ("oferta", "user")

    def __str__(self):
        return f"{self.user_id} legusto {self.oferta.titulo}"


class Periodo_publicacion(models.Model):
    OfertaLaboral = models.ForeignKey(
        OfertaLaboral, on_delete=models.CASCADE, related_name="periodos_publicacion"
    )
    inicio = models.DateTimeField()
    fin = models.DateTimeField()

    class Meta:
        verbose_name = "Periodo Publicación"
        verbose_name_plural = "Periodos Publicación"
        db_table = "Periodos_Publicaciones"

    def activo(self):
        now = timezone.now()
        return self.inicio <= now <= self.fin

    def __str__(self):
        return f" El periodo de actividad para {self.oferta.titulo} es del {self.inicio} al {self.fin}"
