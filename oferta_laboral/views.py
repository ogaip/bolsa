from django.shortcuts import get_object_or_404, render, redirect
from oferta_laboral.forms import OfertaLaboralForm
from .models import OfertaLaboral

# Create your views here.


def inicio(request):
    nick = request.user
    print(nick)
    title = "Bienvenido"
    return render(request, "ofertas/inicio.html", {"title": title, "nickname": nick})


def listar(request):
    nick = request.user
    ofertas = OfertaLaboral.objects.filter(empleador=nick)
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

            return redirect("/ofertas/listarOfertas")
        else:
            return render(
                request,
                "ofertas/crear.html",
                {
                    "title": "Publicar nueva Oferta Laboral",
                    "form": form,
                },
            )
    else:
        nick = request.user
        title = "Publicar nueva Oferta Laboral"
        form = OfertaLaboralForm(request.POST or None)

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
    nick = request.user
    oferta = get_object_or_404(OfertaLaboral, id=id)
    if request.method == "POST":
        form = OfertaLaboralForm(request.POST, instance=oferta)
        if form.is_valid():
            print (form)
            form.save()
            return redirect("/ofertas/listarOfertas")
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
    nick = request.user
    oferta = OfertaLaboral.objects.get(id=id)
    title = f"Ver Oferta Laboral: {oferta.titulo}"

    return render(
        request,
        "ofertas/detalle.html",
        {"title": title, "nickname": nick, "oferta": oferta},
    )


def eliminar(request, id):
    nick = request.user
    oferta = OfertaLaboral.objects.get(id=id)
    oferta.delete()
    return redirect(
        "ofertas/listar", {"nickname": nick, "title": "Oferta Laboral Eliminada"}
    )
