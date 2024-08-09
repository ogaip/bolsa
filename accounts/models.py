# from django.contrib.auth import models
from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Skill")

    def __str__(self):
        return self.nombre


class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Idioma", null=True, )
    nivel = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"
        db_table = "Idiomas"

    def __str__(self):
        return f"{self.nombre} - {self.user_id}"


class Experiencia(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Experiencia"
    )
    empresa = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    funcion = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        db_table = "Experiencias_laborales"

    def __str__(self):
        return f"{self.empresa} - {self.puesto}"


class Estudio(models.Model):
    estado_choice = [
        ("En Curso", "En Curso"),
        ("Finalizado", "Finalizado"),
        ("Abandonado", "Abandonado"),
    ]

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Estudio")
    institucion = models.CharField(max_length=100)
    estado = models.CharField(choices=estado_choice)
    titulo = models.CharField(max_length=100, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    descripcion = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = "Estudio"
        verbose_name_plural = "Estudios"
        db_table = "Estudios"

    def __str__(self):
        return f"{self.institucion} - {self.estado}"


class Perfil(models.Model):
    user = models.OneToOneField(User, related_name="perfil", on_delete=models.CASCADE)
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
    avatar = models.ImageField(upload_to="avatar/", blank=True)
    skills = models.ManyToManyField("Skill", related_name="perfiles")
    idiomas = models.ManyToManyField(Idioma)
    experiencias = models.ManyToManyField(Experiencia)
    estudios = models.ManyToManyField(Estudio)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        db_table = "Perfiles"

    def __str__(self):
        return self.user.username
