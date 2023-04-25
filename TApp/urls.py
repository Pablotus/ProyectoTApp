
from TApp import views

from django.urls import path

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('paciente/', views.paciente, name="paciente"),
    path('buscarpaciente/', views.busqueda_paciente, name="busquedapaciente"),
    path('hoy', views.hoy, name="hoy"),
    path('protocolos', views.protocolos, name="protocolos"),
    path('inicio/eliminar/<eliminar_paciente>', views.eliminar_paciente, name="eliminar_paciente"),
    path('inicio/editar/<numero_paciente>/', views.editar_visita, name="editar_visita"),
    path('busqueda_apellido', views.busqueda_apellido, name="busqueda_apellido"),
    path('buscar_protocolos',views.buscar_protocolos, name="buscar_protocolos"),
    path('calendario', views.calendario, name="calendario"),
]
