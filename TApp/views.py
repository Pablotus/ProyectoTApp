from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime


def inicio(request):

    return render(request, "TApp/index.html")

def paciente(request):

    return render(request, "TApp/paciente.html")

def buscar_paciente(request):

    return render(request, "TApp/buscar_paciente.html")

def hoy(request):

    return render(request, "TApp/hoy.html")


def agregar_paciente(request):
    if request.method == "POST":
        mi_formulario = PacienteForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            paciente_save = Paciente(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                dni=informacion['dni'],
                telefono=informacion['telefono'],
                fecha_nacimiento=informacion['fecha_nacimiento'],
                protocolo=informacion['protocolo'],
                numero_protocolo=informacion['numero_protocolo'],
                ojo_estudio=informacion['ojo_estudio'],
                site_nombre=informacion['site_nombre'],
                site_numero=informacion['site_numero'],
                fecha_rando=informacion['fecha_rando'],

            )
            paciente_save.save()
            return render("TApp/agregar_paciente.html")

    context = {
        "form": PacienteForm()
    }
    return render(request, "TApp/inicio.html", context=context)

def protocolos(request):

    return render(request, "TApp/protocolos.html")