from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from TApp.models import Paciente
from TApp.forms import PacienteForm, BusquedaPacienteForm
from django.db.models import Q


# def busqueda_paciente(request):
#     mi_formulario = BusquedaPacienteForm(request.GET)
#     if mi_formulario.is_valid():
#         informacion = mi_formulario.cleaned_data
#         # Obtener el número de paciente y apellido del formulario
#         numero_paciente = informacion.get('numero_paciente')
#         apellido = informacion.get('apellido')
#         # Filtrar pacientes por número de paciente o apellido
#         if numero_paciente or apellido:
#             pacientes_filtrados = Paciente.objects.filter(
#                 Q(numero_paciente__icontains=numero_paciente) | Q(apellido__icontains=apellido)
#             )
#             context = {
#                 "pacientes": pacientes_filtrados
#             }
#             return render(request, "TApp/resultadosBusqueda.html", context=context)
#
#     # Si el formulario no es válido o no se proporcionaron datos, renderizar la página nuevamente
#     return render(request, "TApp/busca_paciente.html", {"mi_formulario": mi_formulario})



def inicio(request):
    return render(request, "TApp/index.html")


# def paciente(request):
#     return render(request, "TApp/paciente.html")

def paciente(request):

    all_pacientes = Paciente.objects.all()
    context = {
        "pacientes": all_pacientes,
        "form_busqueda": BusquedaPacienteForm(),
    }
    return render(request, "TApp/paciente.html", context=context)



def buscarpaciente(request):
    return render(request, "TApp/buscar_paciente.html")

# def buscar(request):
#     if request.GET["numero_paciente"]:
#         numero_paciente = request.GET['numero_paciente']
#         paciente = Paciente.objects.filter(numero_paciente__icontains=numero_paciente)
#         return render(request, "TApp/resultadosBusqueda.html", {"apellido":apellido, "numero_paciente":numero_paciente})
#     else:
#         respuesta = "no enviaste datos"
#     return HttpResponse(respuesta)


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

def busqueda_paciente(request):
    mi_formulario = BusquedaPacienteForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        pacientes_filtrados = Paciente.objects.filter(numero_paciente__icontains=informacion['numero_paciente'])
        context = {
            "pacientes": pacientes_filtrados,
            "form_busqueda": BusquedaPacienteForm()
        }

        return render(request, "TApp/resultadosBusqueda.html", context=context)


def eliminar_paciente(request, numero_paciente):
        get_paciente = Paciente.objects.get(numero_paciente=numero_paciente)
        get_paciente.delete()

        return redirect("paciente")

def editar_paciente(request, numero_paciente):
    get_paciente = Paciente.objects.get(numero_paciente=numero_paciente)

    if request.method == "POST":
        mi_formulario = PacienteForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            get_paciente.nombre = informacion['nombre']
            get_paciente.numero_paciente = informacion['numero_paciente']

            get_paciente.save()
            return redirect("inicio")


    context = {
        "numero_paciente": numero_paciente,
        "form": PacienteForm(initial={
            "nombre": get_paciente.nombre,
            "numero_paciente": get_paciente.numero_paciente
        })
    }
    return render(request, "TApp/editar_paciente.html", context=context)