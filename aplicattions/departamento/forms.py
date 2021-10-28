from django import forms

class NewDepartamento(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamentos = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=20)