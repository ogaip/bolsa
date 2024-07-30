# from django.contrib.auth import models
from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Skill(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(max_length=500, blank=True)
    ciudad = models.CharField(max_length=20, blank=True)
    pais = models.CharField(max_length=20, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    redes_sociales = models.CharField(max_length=100, blank=True)
    descripcion_personal = models.TextField(max_length=500, blank=True)
    puesto_actual = models.CharField(max_length=100, blank=True)
    ultimo_puesto = models.CharField(max_length=100, blank=True)
    experiencia_laboral = models.TextField(max_length=500, blank=True)
    habilidades_adicionales = models.TextField(max_length=500, blank=True)
    educacion = models.TextField(max_length=500, blank=True)
    referencias = models.TextField(max_length=500, blank=True)
    certificaciones = models.TextField(max_length=500, blank=True)
    intereses = models.TextField(max_length=500, blank=True)
    habilidades_experiencia = models.TextField(max_length=500, blank=True)
    habilidades_conocimientos = models.TextField(max_length=500, blank=True)
    habilidades_conocimientos_adicionales = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True)
    skills = models.ManyToManyField('Skill', related_name='perfiles')

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        

    def __str__(self):
        return self.user.username

