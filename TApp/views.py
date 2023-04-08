from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):

    return render(request, "TApp/index.html")

def paciente(request):

    return render(request, "TApp/paciente.html")

