from django.contrib import admin
from django.db.models.query_utils import subclasses
from django.urls import path, include
from django.utils.regex_helper import normalize
from . import views

app_name="persona_app"

urlpatterns = [
    path(
        '',
        views.inicioView.as_view(),
        name='inicio'
    ),
    path('listar-empleados/',
        views.ListaEmpleados.as_view(),
        name="empleados"
        ),
    path('listar-empleados-admin/',
        views.ListaEmpleadosAdmin.as_view(),
        name="empleados-admin"
        ),

    path(
    'probando2/<shorname>/', 
    views.ListaEmpleadosFiltradas.as_view(),
    name="empleados_area"
    ),
    
    
    path('buscador/', views.buscador.as_view()),
    path('detalle/<pk>/',
          views.detail_empleado.as_view(),
          name="empleado_detail"
        ),

    path('agregar/', 
        views.AgregarCreateView.as_view(),
        name="agregar-empleado"),
    
    
    path(
        'success/',
        views.successView.as_view(),
        name="correcto"
        ),
    path(
        'modificar/<pk>/',
        views.modificarUpdateView.as_view(),
        name="editar_empleado"
        ),
    path(
        'eliminar/<pk>/',
        views.Eliminar_usuario.as_view(),
        name="delete"
        ),
]