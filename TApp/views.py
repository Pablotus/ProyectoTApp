from django.shortcuts import render
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
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Curso(
                nombre=informacion['nombre'],
                apellido=informacion['camada']





            )
            curso_save.save()
            return redirect("AppCoderCursos")

    context = {
        "form": CursoForm()
    }
    return render(request, "TApp/agregar_paciente.html", context=context)

def protocolos(request):

    return render(request, "TApp/protocolos.html")