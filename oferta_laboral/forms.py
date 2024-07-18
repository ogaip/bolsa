

from django import forms
from oferta_laboral.models import ESTADO_CHOICES, OfertaLaboral
from django_prose_editor.fields import ProseEditorFormField, ProseEditorField, ProseEditorWidget


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
            "empleador",
            # Añadir el empleador aqui
        ]

        widgets = {
            "titulo": forms.TextInput(attrs={ "class": "form-control"}),
            # "descripcion": forms.Textarea(attrs={"class": "form-control"}),
            "descripcion": ProseEditorField(),
            # "habilidades_requeridas": forms.Textarea(attrs={"class": "form-control"}),
            "habilidades_requeridas": ProseEditorFormField(),
            "requisitos_laborales": forms.Textarea(attrs={"class": "form-control"}),
            # "beneficios": forms.Textarea(attrs={"class": "form-control"}),
            "beneficios": ProseEditorWidget(attrs={"class": "form-control"}),
            "fecha_limite_postulacion": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "estado": forms.Select(choices=ESTADO_CHOICES),
            "empleado": forms.Select(attrs={"class": "form-control", "disabled" : "disabled"})
            # Añadir el empleador aqui
        }



        errors = {
            "titulo": { "required": "Este campo es obligatorio"},
            "descripcion": {"required": "Este campo es obligatorio"},
            "habilidades_requeridas": {"required": "Este campo es obligatorio"},
            "requisitos_laborales": {"required": "Este campo es obligatorio"},
            "beneficios": {"required": "Este campo es obligatorio"},
            "fecha_limite_postulacion": {"required": "Este campo es obligatorio"},
            "estado": {"required": "Este campo es obligatorio"},
            "empleador": {"required": "Este campo es obligatorio"},
            # Añadir el empleador aqui
        }
