from django.views.generic.base import TemplateView
from aplicattions.departamento.models import departamento
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import empleado
from django.urls import reverse_lazy
from .forms import PruebaForm

# Create your views here.

class inicioView(TemplateView):
    """" Vista que carga pagina principal """
    template_name = 'inicio.html'

class ListaEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'name'
    context_object_name = 'empleado'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista=empleado.objects.filter(
        full_name__icontains = palabra_clave,
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/admin_edit.html'
    paginate_by = 10
    ordering = 'name'
    context_object_name = 'empleado'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista=empleado.objects.filter(
        full_name__icontains = palabra_clave,
        )
        return lista


class ListaEmpleadosFiltradas(ListView):
    """  Empleados de un area """
    template_name = 'persona/list.html'
    context_object_name = 'empleado'
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = empleado.objects.filter(
            departamento_short_name=area
        )
        return lista


    def get_queryset(self):
        area = self.kwargs['shorname']
        lista=empleado.objects.filter(
        Departamento__short_name=area
    )
        return lista

class buscador(ListView):
    template_name='persona/buscador.html'
    context_object_name='empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista=empleado.objects.filter(
        name = palabra_clave
    )
        
        return lista


class detail_empleado(DetailView):
    model = empleado
    template_name = "persona/detalle.html"

    def get_context_data(self, **kwargs):
        context = super(detail_empleado, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado'
        return context


class AgregarCreateView(CreateView):
    model = empleado
    template_name = "persona/add.html"
    fields = [
        'name',
        'short_name',
        'full_name',
        'job',
        'Departamento',
        'habilidad',
        'avatar'
    ]
    success_url = reverse_lazy("persona_app:empleados-admin")

class successView(TemplateView):
    template_name='persona/pantalla.html'

class modificarUpdateView(UpdateView):
    model = empleado
    template_name = "persona/modificar.html"
    fields=('__all__')
    success_url = reverse_lazy('persona_app:empleados-admin')


class Eliminar_usuario(DeleteView):
    model = empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados-admin')
