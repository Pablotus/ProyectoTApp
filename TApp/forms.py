from django import forms

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
    investigador=forms.CharField(max_length=40)
    fecha_visita = forms.DateField()
    visita = forms.CharField(max_length=8)
    fecha_rando = forms.DateField()


class BusquedaPacienteForm(forms.Form):
    numero_paciente = forms.CharField(required=False)


class BusquedaApellidoForm(forms.Form):
    apellido = forms.CharField(required=False, max_length=40)

class BusquedaProtocoloForm(forms.Form):
    nombre = forms.CharField(max_length=40)
