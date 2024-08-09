from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Perfil, Skill

def registro(request):
    """esta funcion es para registrar un usuario nuevo
    si la solicitud es de tipo POST:
        instanciamos el formulario de registro en la varialbe fom, validamos los datos recibidos, guardamos los datos en la DB y redireccionamos al usuario a la pagina de logeo para que ingrese sus datos y si algo no esta bien lo devolemos al formulario de registro con los mensajes de error.

    si la solicitud es de tipo GET:
        se cargar el formulario



    Args:
        request (request): contiene todos los datos sobre una solicitud HTTP

    Returns:
        render: renderisa la vista
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
        else:
            return render(
                request,
                "registration/registro.html",
                {
                    "form": form,
                    "error": "form.errors",
                },
            )
    else:
        form = UserCreationForm()
    return render(request, "registration/registro.html", {"form": form})


# Create your views here.

def login_view(request):
    """Esta función es para el login de un usuario
        valida el usuario y la contraseña

    Args:
        request (requset): contiene todos los datos sobre una solicitud HTTP

    Returns:
        render: renderiza la vista
    """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect("perfil")
            else:
                return render(request, "registration/login.html", {"form": form, "error": "Usuario o contraseña incorrecta"})
        else:
            return render(request, "registration/login.html", {"form": form, "error": form.errors})
    else:
        form = AuthenticationForm()


@login_required
def logout_view(request):
    """Esta función es para el logout de un usuario

    Args:
        request (requset): contiene todos los datos sobre una solicitud HTTP

    Returns:
        redirect: redirecciona al login
    """
    logout(request)
    return redirect("login")


@login_required
def ver_perfil(request):
    """Esta función es para mostrar el profile del usuario logueado

    Args:
        request (requset): contiene todos los datos sobre una solicitud HTTP

    Returns:
        render: renderiza la vista
    """
    user = request.user
    title = "Perfil de "
    perfil= Perfil.objects.filter(user__username=user).values()
    userdata= User.objects.filter(username=user).values()
    skill = Skill.objects.filter(usuario__id= user.id).values()
    
    
    return render(request, "profile/profile.html", {
        "nickname": user.username,
        "title": title + user.username,
        "userdata": userdata,
        "perfil": perfil,
        "skill": skill,
        

    })


@login_required
def editar_perfil(request):
    user = request.user
    if request.method == 'POST':
        editarPerfilForm = UserChangeForm(request.POST, instance=user)
        print(editarPerfilForm)
        profile_form = UserCreationForm(request.POST, instance=user)
        if editarPerfilForm.is_valid():
            editarPerfilForm.save()
            return redirect('perfil')
    else:
        editarPerfilForm = UserChangeForm(instance=user)
        profile_form = UserCreationForm(instance=user)

    return render(request, 'profile/profile_edit.html', {
        "title": "Editar tu perfil",
        'form': editarPerfilForm,
        'nickname': user,
        'crearForm': profile_form,
    })
