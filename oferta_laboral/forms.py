

from django import forms
from oferta_laboral.models import ESTADO_CHOICES, OfertaLaboral
from tinymce.widgets import TinyMCE


# Create your forms here.


class OfertaLaboralForm(forms.ModelForm):
    class Meta:
        model = OfertaLaboral
        fields = [
            "titulo",
            "descripcion",
            "habilidades_requeridas",
            "requisitos_laborales",
            "beneficios",
            "fecha_limite_postulacion",
            "estado",
            # "user",
            # Añadir el empleador aqui
        ]

        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            # "descripcion": (attrs={"class": "form-control"}),
            "descripcion": TinyMCE(attrs={"class": "form-control", "type": "textArea"}),
            # "habilidades_requeridas": (attrs={"class": "form-control"}),
            "habilidades_requeridas": TinyMCE(),
            "requisitos_laborales": TinyMCE(attrs={"class": "form-control"}),
            # "beneficios": (attrs={"class": "form-control"}),
            "beneficios": TinyMCE(attrs={"class": "form-control"}),
            "fecha_limite_postulacion": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "estado": forms.Select(choices=ESTADO_CHOICES),
            "user": forms.TextInput(attrs={"class": "form-control", 'hidden': ' True'}),
            # Añadir el empleador aqui
        }

        errors = {
            "titulo": {"required": "Este campo es obligatorio"},
            "descripcion": {"required": "Este campo es obligatorio"},
            "habilidades_requeridas": {"required": "Este campo es obligatorio"},
            "requisitos_laborales": {"required": "Este campo es obligatorio"},
            "beneficios": {"required": "Este campo es obligatorio"},
            "fecha_limite_postulacion": {"required": "Este campo es obligatorio"},
            "estado": {"required": "Este campo es obligatorio"},
            "user": {"required": "Este campo es obligatorio"},
            # Añadir el empleador aqui
        }
