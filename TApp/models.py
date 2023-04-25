from django.db import models

class Paciente(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    protocolo = models.CharField(max_length=40)
    numero_protocolo= models.CharField(max_length=40)
    numero_paciente = models.CharField(max_length=40, unique=True)
    ojo_estudio = models.CharField(max_length=2)
    site_nombre = models.CharField(max_length=40)
    site_numero = models.CharField(max_length=40)
    investigador = models.CharField(max_length=40)
    fecha_visita = models.DateField()
    visita = models.CharField(max_length=8)
    fecha_rando = models.DateField()
    comentario = models.CharField(max_length=80)

    # def __str__(self):
    #     return f"nombre: {self.nombre}, apellido: {self.apellido}"

class Protocolo(models.Model):
    nombre= models.CharField(max_length=40)
    codigo= models.CharField(max_length=40)
    site= models.CharField(max_length=40)
    site_numero= models.CharField(max_length=40)
    invest_princ= models.CharField(max_length=40)
    invest_enmasc= models.CharField(max_length=150)
    invest_NOenmasc= models.CharField(max_length=150)

    # def __str__(self):
    #     return f"nombre: {self.nombre}, apellido: {self.apellido}"