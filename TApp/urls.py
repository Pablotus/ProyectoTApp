
from TApp import views

from django.urls import path

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('paciente/', views.paciente, name="paciente"),
    path('buscar paciente', views.buscar_paciente, name="buscar_paciente"),
    path('hoy', views.hoy, name="hoy"),
    path('protocolos', views.protocolos, name="protocolos"),
]
