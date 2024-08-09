from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from accounts.models import Perfil
from .models import OfertaLaboral
from django.contrib.auth.decorators import login_required


# Create your views here.


user = get_user_model()


@login_required
def inicio(request):
    nick = request.user
    user = User.objects.filter(username=request.user).values()
    perfil = Perfil.objects.filter(user__username=nick)
    print(perfil)

    return render(
        request,
        "ofertas/inicio.html",
        {
            "nickname": request.user,
            "userdata": user,
            "title": "Bienvenido",
            "perfil": perfil,
        },
    )


@login_required
def listar(request):
    ofertas = OfertaLaboral.objects.all()
    nick = request.user
    perfil = Perfil.objects.filter(user__username=nick)
    print(perfil)
    title = "Listado de Ofertas Laborales"

    return render(
        request,
        "ofertas/listar.html",
        {
            "nickname": nick,
            "perfil": perfil,
            "title": title,
            "ofertas": ofertas,
        },
    )


@login_required
def crear(request):
    form = Crea
    if request.method == "POST":
        form = OfertaLaboralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ofertas:listar")
        else:
            return render(request, "ofertas/crear.html", {"form": form})
    else:

        title = "Crear Nueva Oferta Laboral"
    return render(request, "ofertas/crear.html", {"title": title})


def editar(request, id):
    return render(request, "ofertas/editar.html", {"id": id})


def eliminar(request, id):
    return render(request, "ofertas/eliminar.html", {"id": id})


def ver(request, id):
    return render(request, "ofertas/detalle.html", {"id": id})
