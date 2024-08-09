from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Perfil, Skill, Idioma, Experiencia, Estudio

# Register your models here.
class SkillAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario')
    



class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = "Perfiles"



class UserAdmin(BaseUserAdmin):
    list_display = ('id','username', 'email', 'is_staff', 'is_superuser', 'first_name', 'last_name', 'perfil')
    
    inlines = [ PerfilInline ]


class IdiomaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'user_id', 'nivel')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Idioma, IdiomaAdmin)
admin.site.register(Estudio)
admin.site.register(Experiencia)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Perfil)


