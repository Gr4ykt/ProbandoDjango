from django.shortcuts import render
from django.views.generic import *
from django.views.generic import FormView
from .forms import NewDepartamento
from .models import departamento

# Create your views here.
class DepartamentoListeview(ListView):
    model = departamento
    template_name = "departamento/lista.html"
    context_object_name = "departamento"


class probando(TemplateView):
    template_name = "departamento/plantilla1.html"

class Nuevo_departamento(FormView):
    template_name = "departamento/new_departamento.html"
    forms_class = NewDepartamento
    success_url = '/'

    def form_valid(self, form):
        return super(Nuevo_departamento, self).form_valid(form)