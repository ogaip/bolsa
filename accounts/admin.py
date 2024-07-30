from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Perfil, Skill

# Register your models here.

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = "Perfiles"


class UserAdmin(BaseUserAdmin):
    
    inlines = [ PerfilInline ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(User, UserAdmin)
admin.site.register(Skill)
# admin.site.register(Perfil, PerfilAdmin)


