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
from datetime import datetime, timedelta
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required




@login_required
def calendario(request):
    fecha_inicio = timezone.now().date()
    fecha_fin = fecha_inicio + timedelta(days=90)
    pacientes = Paciente.objects.filter(fecha_visita__range=[fecha_inicio, fecha_fin]).order_by('fecha_visita')
    return render(request, 'TApp/calendario.html', {'pacientes': pacientes})



@login_required
def hoy(request):
    fecha_hoy = datetime.today().date()
    pacientes = Paciente.objects.filter(fecha_visita=fecha_hoy)

    return render(request, 'TApp/hoy.html', {'pacientes': pacientes})

def inicio(request):
    return render(request, "TApp/index.html")

@login_required
def paciente(request):

    all_pacientes = Paciente.objects.all()
    context = {
        "pacientes": all_pacientes,
        "form_busqueda": BusquedaPacienteForm(),
    }
    return render(request, "TApp/paciente.html", context=context)
@login_required
def buscarpaciente(request):
    return render(request, "TApp/buscar_paciente.html")


@login_required
def protocolos(request):

    all_protocolos = Protocolo.objects.all()
    context = {
        "protocolos": all_protocolos,
    }
    return render(request, "TApp/protocolos.html", context=context)

@login_required
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

@login_required
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

@login_required
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
    return render(request, "TApp/protocolos.html", context=context)




def eliminar_paciente(request, numero_paciente):
        get_paciente = Paciente.objects.get(numero_paciente=numero_paciente)
        get_paciente.delete()

        return redirect("paciente")

@login_required
def editar_visita(request, numero_paciente):
    get_paciente = Paciente.objects.get(numero_paciente=numero_paciente)


    if request.method == "POST":
        mi_formulario = PacienteForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            get_paciente.fecha_visita= informacion['fecha_visita']
            get_paciente.visita = informacion['visita']
            get_paciente.comentario = informacion['comentario']
            get_paciente.save()

            return redirect("paciente")


    context = {
        "numero_paciente": numero_paciente,
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
            "comentario": get_paciente.comentario,
        })
    }
    return render(request, "TApp/editar_visita.html", context=context)









