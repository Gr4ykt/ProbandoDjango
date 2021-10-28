from django import forms
from .models import empleado

class PruebaForm(forms.ModelForm):
    """Form defiPruebaFormDELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""
        model = empleado
        fields = (
            'name',
            'short_name',
            'job',
            'Departamento',
            'habilidad'
        )
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'placeholder' : "Ingrese nombre aqui"
                }
            )
        }
