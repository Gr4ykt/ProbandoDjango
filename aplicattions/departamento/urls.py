from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "departamento_app"

urlpatterns = [
    path('prueba/', views.probando.as_view()),
    path('nuevo-depa/', views.Nuevo_departamento.as_view()),
    path('departamento-list/', views.DepartamentoListeview.as_view(),
    name="Departamento_list"),
    
]