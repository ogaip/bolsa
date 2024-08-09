"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views as ofertas_views


urlpatterns = [
    path("", ofertas_views.inicio, name="inicio"),
    #####################
    path("listarOfertas/", ofertas_views.listar, name="listar"),
    path("crearOferta/", ofertas_views.crear, name="crear"),
    path("editarOferta/<int:id>/", ofertas_views.editar, name="editar"),
    path("eliminarOferta/<int:id>/", ofertas_views.eliminar, name="eliminar"),
    path("verOferta/<int:id>/", ofertas_views.ver, name="ver"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
