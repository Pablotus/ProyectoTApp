from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from TApp.models import Paciente, Protocolo
from TApp.forms import PacienteForm, BusquedaPacienteForm, BusquedaApellidoForm, BusquedaProtocoloForm
from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import BusquedaProtocoloForm
from .models import Protocolo
import calendar
from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from datetime import datetime
from django.utils import timezone

from django.forms import ModelForm
from .models import Paciente




def hoy(request):
    pacientes = Paciente.objects.filter(fecha_visita=timezone.now().date())

    return render(request, 'TApp/hoy.html', {'pacientes': pacientes})



def inicio(request):
    return render(request, "TApp/index.html")

def paciente(request):

    all_pacientes = Paciente.objects.all()
    context = {
        "pacientes": all_pacientes,
        "form_busqueda": BusquedaPacienteForm(),
    }
    return render(request, "TApp/paciente.html", context=context)

def buscarpaciente(request):
    return render(request, "TApp/buscar_paciente.html")

# def hoy(request):
#     return render(request, "TApp/hoy.html")

def protocolos(request):

    all_protocolos = Protocolo.objects.all()
    context = {
        "protocolos": all_protocolos,
    }
    return render(request, "TApp/protocolos.html", context=context)
def busqueda_apellido(request):
    if request.method == 'GET' and 'apellido' in request.GET:
        mi_formulario2 = BusquedaApellidoForm(request.GET)
        if mi_formulario2.is_valid():
            informacion2 = mi_formulario2.cleaned_data
            pacientes_filtrados2 = Paciente.objects.filter(apellido__icontains=informacion2['apellido'])
            context2 = {
                "pacientes": pacientes_filtrados2,
                "form_busqueda": BusquedaApellidoForm()
            }
            return render(request, "TApp/resultadosBusquedaApellido.html", context=context2)
    else:
        form_busqueda = BusquedaApellidoForm()
        context = {
            "pacientes": None,
            "form_busqueda": form_busqueda
        }
        return render(request, "TApp/resultadosBusquedaApellido.html", context=context)

def busqueda_paciente(request):
    if request.method == 'GET' and 'numero_paciente' in request.GET:
        mi_formulario2 = BusquedaPacienteForm(request.GET)
        if mi_formulario2.is_valid():
            informacion2 = mi_formulario2.cleaned_data
            pacientes_filtrados2 = Paciente.objects.filter(numero_paciente__icontains=informacion2['numero_paciente'])
            context2 = {
                "pacientes": pacientes_filtrados2,
                "form_busqueda": BusquedaPacienteForm()
            }
            return render(request, "TApp/resultadosBusqueda.html", context=context2)
    else:
        form_busqueda = BusquedaPacienteForm()
        context = {
            "pacientes": None,
            "form_busqueda": form_busqueda
        }
        return render(request, "TApp/resultadosBusqueda.html", context=context)


@require_http_methods(["GET"])
def buscar_protocolos(request):
    form_busqueda = BusquedaProtocoloForm(request.GET)
    protocolos_filtrados = None
    if form_busqueda.is_valid():
        informacion = form_busqueda.cleaned_data
        protocolos_filtrados = Protocolo.objects.filter(nombre__icontains=informacion['nombre'])
    context = {
        "protocolos": protocolos_filtrados,
        "form_busqueda": form_busqueda
    }
    return render(request, "TApp/resultadosBusquedaProtocolo.html", context=context)


# def agregar_paciente(request):
#     if request.method == 'POST':
#
#         miFormulario = PacienteForm(request.POST)
#
#         if miFormulario.is_valid():
#             informacion = miFormulario.cleaned_data
#
#             paciente = Paciente(nombre=informacion['nombre'],
#                                 apellido=informacion['apellido'],
#                                 dni=informacion['dni'],
#                                 telefono=informacion['telefono'],
#                                 fecha_nacimiento=informacion['fecha_nacimiento'],
#                                 protocolo=informacion['protocolo'],
#                                 numero_protocolo=informacion['numero_protocolo'],
#                                 numero_paciente=informacion['numero_paciente'],
#                                 ojo_estudio=informacion['ojo_estudio'],
#                                 site_nombre=informacion['site_nombre'],
#                                 site_numero=informacion['site_numero'],
#                                 investigador=informacion['site_numero'],
#                                 fecha_rando=informacion['fecha_rando'],
#                                 )
#
#             paciente.save()
#             return render(request, "TApp/inicio.html")
#     else:
#         miFormulario = PacienteForm()
#
#     return render(request, "TApp/agregar_paciente.html", {"miFormulario": miFormulario})




def eliminar_paciente(request, numero_paciente):
        get_paciente = Paciente.objects.get(numero_paciente=numero_paciente)
        get_paciente.delete()

        return redirect("paciente")

# def editar_visita(request, fecha_visita, visita, numero_paciente, apellido, nombre):
#     get_numero_paciente = Paciente.objects.get(numero_paciente=numero_paciente)
#     get_apellido = Paciente.objects.get(apellido=apellido)
#     get_nombre = Paciente.objects.get(nombre=nombre)
#     get_fecha = Paciente.objects.get(fecha_visita=fecha_visita)
#     get_visita = Paciente.objects.get(visita=visita)
#
#     if request.method == "POST":
#         mi_formulario = PacienteForm(request.POST)
#
#         if mi_formulario.is_valid():
#             informacion = mi_formulario.cleaned_data
#             get_numero_paciente.numero_paciente = informacion['Numero de paciente']
#             get_apellido.apellido = informacion['Apellido']
#             get_nombre.nombre = informacion['Nombre']
#             get_fecha.fecha_visita= informacion['Fecha visita proxima']
#             get_visita.visita = informacion['visita']
#
#
#             get_numero_paciente.save()
#             get_apellido.save()
#             get_nombre.save()
#             get_fecha.save()
#             get_visita.save()
#             return redirect("inicio")
#
#
#     context = {
#         "numero_paciente": numero_paciente,
#         "apellido": apellido,
#         "nombre": nombre,
#         "fecha_visita": fecha_visita,
#         "visita": visita,
#         "form": PacienteForm(initial={
#             "numero_paciente": get_numero_paciente.numero_paciente,
#             "apellido": get_apellido.apellido,
#             "nombre": get_nombre.nombre,
#             "fecha_visita": get_fecha.fecha_visita,
#             "visita": get_visita.visita,
#         })
#     }
#     return render(request, "TApp/editar_visita.html", context=context)

# def editar_visita(request, fecha_visita, visita, numero_paciente, apellido, nombre):
#     get_paciente = Paciente.objects.get(numero_paciente=numero_paciente, apellido=apellido,nombre=nombre,fecha_visita=fecha_visita,visita=visita)
#
#
#     if request.method == "POST":
#         mi_formulario = PacienteForm(request.POST)
#
#         if mi_formulario.is_valid():
#             informacion = mi_formulario.cleaned_data
#
#             get_paciente.numero_paciente = informacion['Numero de paciente']
#             get_paciente.apellido = informacion['Apellido']
#             get_paciente.nombre = informacion['Nombre']
#             get_paciente.fecha_visita= informacion['Fecha visita proxima']
#             get_paciente.visita = informacion['visita']
#
#             get_paciente.save()
#
#             return redirect("inicio")
#
#
#     context = {
#         "numero_paciente": numero_paciente,
#         "apellido": apellido,
#         "nombre": nombre,
#         "fecha_visita": fecha_visita,
#         "visita": visita,
#         "form": PacienteForm(initial={
#             "numero_paciente": get_paciente.numero_paciente,
#             "apellido": get_paciente.apellido,
#             "nombre": get_paciente.nombre,
#             "fecha_visita": get_paciente.fecha_visita,
#             "visita": get_paciente.visita,
#         })
#     }
#     return render(request, "TApp/editar_visita.html", context=context)

def editar_visita(request, fecha_visita, visita):
    get_paciente = Paciente.objects.get(fecha_visita=fecha_visita, visita=visita)


    if request.method == "POST":
        mi_formulario = PacienteForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            get_paciente.fecha_visita= informacion['fecha_visita']
            get_paciente.visita = informacion['visita']
            get_paciente.save()

            return redirect("paciente")


    context = {
        "fecha_visita": fecha_visita,
        "visita": visita,
        "form": PacienteForm(initial={
            "numero_paciente": get_paciente.numero_paciente,
            "apellido": get_paciente.apellido,
            "dni": get_paciente.dni,
            "telefono": get_paciente.telefono,
            "fecha_nacimiento": get_paciente.fecha_nacimiento,
            "protocolo": get_paciente.protocolo,
            "numero_protocolo": get_paciente.numero_protocolo,
            "ojo_estudio": get_paciente.ojo_estudio,
            "site_nombre": get_paciente.site_nombre,
            "site_numero": get_paciente.site_numero,
            "investigador": get_paciente.investigador,
            "fecha_rando": get_paciente.fecha_rando,
            "nombre": get_paciente.nombre,
            "fecha_visita": get_paciente.fecha_visita,
            "visita": get_paciente.visita,
        })
    }
    return render(request, "TApp/editar_visita.html", context=context)









