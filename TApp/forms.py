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
    fecha_rando = forms.DateField()

#
# class ProtocoloForm(forms.Form):
#         nombre = models.CharField(max_length=40)
#         codigo = models.CharField(max_length=40)