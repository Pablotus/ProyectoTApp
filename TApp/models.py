from django.db import models

class Paciente(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField(unique=True)
    telefono = models.IntegerField(unique=True)
    fecha_nacimiento = models.DateField()
    protocolo = models.CharField(max_length=40)
    numero_protocolo= models.IntegerField
    numero_paciente = models.IntegerField(unique=True)
    ojo_estudio = models.CharField(max_length=2)
    site_nombre = models.CharField(max_length=40)
    site_numero = models.IntegerField
    fecha_rando = models.DateField()


    # def __str__(self):
    #     return f"nombre: {self.nombre}, apellido: {self.apellido}"

class Protocolo(models.Model):
    nombre= models.CharField(max_length=40)
    codigo= models.CharField(max_length=40)

    # def __str__(self):
    #     return f"nombre: {self.nombre}, apellido: {self.apellido}"