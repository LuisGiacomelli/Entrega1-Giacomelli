from django.db import models

# Create your models here.

class Reserva(models.Model):
    nombre = models.CharField(max_length=60)
    cant_especies = models.IntegerField()
    ubicacion = models.CharField(max_length=60)

class Animal(models.Model):
    especie = models.CharField(max_length=60)
    cant = models.IntegerField()
    reserva = models.CharField(max_length=60)

class Cuidador(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    mail = models.EmailField()
    especialidad = models.CharField(max_length=60)