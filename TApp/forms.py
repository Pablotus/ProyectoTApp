from django import forms
from django.forms import ModelForm
from .models import Paciente



class PacienteForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.CharField(max_length=40)
    telefono = forms.CharField(max_length=40)
    fecha_nacimiento = forms.DateField()
    protocolo = forms.CharField(max_length=40)
    numero_protocolo = forms.CharField(max_length=40)
    numero_paciente = forms.CharField(max_length=40)
    ojo_estudio = forms.CharField(max_length=2)
    site_nombre = forms.CharField(max_length=40)
    site_numero = forms.CharField(max_length=40)
    investigador = forms.CharField(max_length=40)
    fecha_rando = forms.DateField()
    fecha_visita = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    visita = forms.CharField(max_length=8)
    comentario = forms.CharField(required=False,max_length=80)


class BusquedaPacienteForm(forms.Form):
    numero_paciente = forms.CharField(required=False)


class BusquedaApellidoForm(forms.Form):
    apellido = forms.CharField(required=False, max_length=40)

class BusquedaProtocoloForm(forms.Form):
    nombre = forms.CharField(max_length=40)



from django.forms import ModelForm
from .models import Paciente

class PacienteVisitaForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['numero_paciente', 'apellido', 'nombre', 'fecha_visita', 'visita']

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance:
            kwargs.setdefault('initial', {})
            kwargs['initial'].update({
                'numero_paciente': instance.numero_paciente,
                'apellido': instance.apellido,
                'nombre': instance.nombre,
                'fecha_visita': instance.fecha_visita,
                'visita': instance.visita,
            })
        super().__init__(*args, **kwargs)
