from django.contrib import admin

# Register your models here.


from accounts.models import Perfil, Skill, Idioma, Experiencia, Estudio

class SkillAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario')

    


    