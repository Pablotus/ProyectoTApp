
from TApp.views import *

from django.urls import path

urlpatterns = [
    path('', inicio),
    path('paciente/', paciente),
]
