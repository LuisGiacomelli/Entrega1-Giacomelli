from django.shortcuts import render
from django.http import HttpResponse
from AppEntre2.models import *

# Create your views here.

def inicio(request):
    return HttpResponse("Esta es la vista de bienvenida")

def reserva(request):

    res1 = Reserva(nombre="Parque Nacional Iguazú", cant_especies="775", ubicacion="Misiones")
    res1.save()

    return HttpResponse(f"La Reserva {res1.nombre} contiene {res1.cant_especies} especies y esta ubicada en {res1.ubicacion}.")

def animal(request):

    anim1 = Animal(especie="Yaguareté", cant="20", reserva="Parque Nacional Iguazú")
    anim1.save()

    return HttpResponse(f"Especie: {anim1.especie}. cantidad: {anim1.cant}. reserva: {anim1.reserva}.")

def cuidador(request):

    cuida1 = Cuidador(nombre="Julian", apellido="Perez", mail="jperez@reserv.com", especialidad="Mamiferos")
    cuida1.save()

    return HttpResponse("Cuidadores")