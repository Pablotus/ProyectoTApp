from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from TApp.models import Paciente
from TApp.forms import PacienteForm


def inicio(request):
    return render(request, "TApp/index.html")


def paciente(request):
    return render(request, "TApp/paciente.html")

def buscarpaciente(request):
    return render(request, "TApp/buscar_paciente.html")
def buscar(request):
    if request.GET["numero_paciente"]:

    #respuesta = f"Estoy buscando el paciente nro: {request.GET['numero_paciente'] }"
        numero_paciente = request.GET ['numero_paciente']
        paciente = Paciente.objects.filter(numero_paciente__icontains=numero_paciente)
        return render(request, "TApp/resultadosBusqueda.html", {"paciente":paciente, "numero_paciente": numero_paciente})
    else:
        respuesta = "no enviaste datos"
    return HttpResponse(respuesta)


def hoy(request):
    return render(request, "TApp/hoy.html")


# def agregar_paciente(request):
#     if request.method == "POST":
#         mi_formulario = PacienteForm(request.POST)
#         print(mi_formulario)
#
#         if mi_formulario.is_valid:
#             informacion = mi_formulario.cleaned_data
#
#             paciente = Paciente(
#                 nombre=informacion['nombre'],
#                 apellido=informacion['apellido'],
#                 dni=informacion['dni'],
#                 telefono=informacion['telefono'],
#                 fecha_nacimiento=informacion['fecha_nacimiento'],
#                 protocolo=informacion['protocolo'],
#                 numero_protocolo=informacion['numero_protocolo'],
#                 ojo_estudio=informacion['ojo_estudio'],
#                 site_nombre=informacion['site_nombre'],
#                 site_numero=informacion['site_numero'],
#                 fecha_rando=informacion['fecha_rando'],
#
#             )
#             paciente.save()
#             return render(request, "TApp/inicio.html")
#         else:
#             miFormulario = PacienteForm()
#
#         return render(request, "TApp/agregar_paciente.html", {"miFormulario": miFormulario})


def protocolos(request):
    return render(request, "TApp/protocolos.html")


def agregar_paciente(request):
    if request.method == 'POST':

        miFormulario = PacienteForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            paciente = Paciente(nombre=informacion['nombre'],
                                apellido=informacion['apellido'],
                                dni=informacion['dni'],
                                telefono=informacion['telefono'],
                                fecha_nacimiento=informacion['fecha_nacimiento'],
                                protocolo=informacion['protocolo'],
                                numero_protocolo=informacion['numero_protocolo'],
                                numero_paciente=informacion['numero_paciente'],
                                ojo_estudio=informacion['ojo_estudio'],
                                site_nombre=informacion['site_nombre'],
                                site_numero=informacion['site_numero'],
                                fecha_rando=informacion['fecha_rando'],
                                )

            paciente.save()
            return render(request, "TApp/inicio.html")
    else:
        miFormulario = PacienteForm()

    return render(request, "TApp/agregar_paciente.html", {"miFormulario": miFormulario})
