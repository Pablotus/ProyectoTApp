
from TApp import views

from django.urls import path

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('paciente/', views.paciente, name="paciente"),
    path('buscarpaciente/', views.buscarpaciente, name="buscarpaciente"),
    path('buscar/', views.buscar),
    path('hoy', views.hoy, name="hoy"),
    path('protocolos', views.protocolos, name="protocolos"),
    path('agregar_paciente', views.agregar_paciente, name="agregar_paciente"),
]
