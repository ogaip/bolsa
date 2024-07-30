from django.shortcuts import get_object_or_404, render, redirect
from oferta_laboral.forms import OfertaLaboralForm
from .models import OfertaLaboral
from .models import User

# Create your views here.


def inicio(request):
    nick = request.user
    print(nick)
    title = "Bienvenido"
    return render(request, "ofertas/inicio.html", {"title": title, "nickname": nick})


def listar(request):
    nick = request.user
    ofertas = OfertaLaboral.objects.all()
    print(ofertas)
    title = "Listado de Ofertas Laborales"

    return render(
        request,
        "ofertas/listar.html",
        {"title": title, "nickname": nick, "ofertas": ofertas},
    )


def crear(request):
    if request.method == "POST":
        form = OfertaLaboralForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/ofertas/listar.html")
        else:
            return render(
                request,
                "ofertas/crear.html",
                {
                    "title": "Publicar nueva Oferta Laboral - error",
                    "form": form,
                    "error": form.errors,
                    "nickname": request.user
                })

    else:
        nick = request.user
        title = "Publicar nueva Oferta Laboral"
        form = OfertaLaboralForm()

        return render(
            request,
            "ofertas/crear.html",
            {
                "nickname": nick,
                "title": title,
                "form": form,
            },
        )


def editar(request, id):
    print (request.POST)
    nick = request.user
    oferta = get_object_or_404(OfertaLaboral, id=id)
    if request.method == "POST":
        form = OfertaLaboralForm(request.POST, instance=oferta)
        if form.is_valid():
            form.save()
            return redirect("listar")
        else:
            return render(
                request,
                "ofertas/editar.html",
                {
                    "title": f"Editar Oferta Laboral: {oferta.titulo}",
                    "form": form,
                    "oferta": oferta,
                    "errors": form.errors,
                    "nickname": nick,
                },
            )
    return render(
        request,
        "ofertas/editar.html",
        {
            "title": f"Editar Oferta Laboral: {oferta.titulo}",
            "oferta": oferta,
            "form": OfertaLaboralForm(instance=oferta),
            "nickname": nick,
        },
    )


def ver(request, id):
    oferta = OfertaLaboral.objects.filter(id=id)
    print (oferta.values())
    nick = User.objects.get(id=id)
    
    title = "Oferta Laboral"
    return render(
        request,
        "ofertas/detalle.html",
        {
            "title": title, 
            "nickname": nick, 
            "oferta": oferta},
    )


def eliminar(request, id):
    nick = request.user
    oferta = OfertaLaboral.objects.get(id=id)
    oferta.delete()
    return redirect(
        "ofertas/listar", {"nickname": nick,
                           "title": "Oferta Laboral Eliminada"}
    )
