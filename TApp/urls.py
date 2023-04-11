
from TApp import views

from django.urls import path

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('paciente/', views.paciente, name="paciente"),
    path('buscarpaciente/', views.busqueda_paciente, name="busquedapaciente"),
    #path('resultadobusqueda', views.busqueda_paciente, name="resultadobusqueda"),
    #path('buscar/', views.buscar),
    path('hoy', views.hoy, name="hoy"),
    path('protocolos', views.protocolos, name="protocolos"),
    path('inicio/agregar/agregar_paciente', views.agregar_paciente, name="agregar_paciente"),
    path('inicio/eliminar/<eliminar_paciente>', views.eliminar_paciente, name="eliminar_paciente"),
    path('inicio/editar/<editar_paciente>', views.editar_paciente, name="editar_paciente"),
]
