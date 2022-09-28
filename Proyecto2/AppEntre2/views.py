from django.shortcuts import render
from django.http import HttpResponse
from AppEntre2.forms import Animalform, Cuidadorform, Reservaform
from AppEntre2.models import *

# Create your views here.

def inicio(request):
    return render(request,"AppEntre2/inicio.html")

def reserva(request):

    res1 = Reserva(nombre="Parque Nacional Iguazú", cant_especies="775", ubicacion="Misiones")
    res1.save()

    return render(request,"AppEntre2/reserva.html")

def animal(request):

    anim1 = Animal(especie="Yaguareté", cant="20", reserva="Parque Nacional Iguazú")
    anim1.save()

    return render(request,"AppEntre2/animal.html")

def cuidador(request):

    cuida1 = Cuidador(nombre="Julian", apellido="Perez", mail="jperez@reserv.com", especialidad="Mamiferos")
    cuida1.save()

    return render(request,"AppEntre2/cuidador.html")

def reservaform(request):
    
    if request.method == "POST":
        
        form1 = Reservaform(request.POST)
        
        if form1.is_valid():
            
            info = form1.cleaned_data
            
            reserva = Reserva(nombre=info["nombre"], cant_especies=info["cant_especies"], ubicacion=info["ubicacion"])
            
            reserva.save()
            
            return render(request,"AppEntre2/inicio.html")
        
    else:
        
        form1 = Reservaform()
        
    return render(request, "AppEntre2/reservaform.html", {"form1":form1})

def animalform(request):

    if request.method == "POST":

        form1 = Animalform(request.POST)

        if form1.is_valid():

            info = form1.cleaned_data

            animal = Animal(especie=info["especie"], cant=info["cant"], reserva=info["reserva"])

            animal.save()

            return render(request,"AppEntre2/inicio.html")

    else:

        form1 = Animalform()

    return render(request, "AppEntre2/animalform.html", {"form1":form1})

def cuidadorform(request):

    if request.method == "POST":

        form1 = Cuidadorform(request.POST)

        if form1.is_valid():

            info = form1.cleaned_data

            cuidador = Cuidador(nombre=info["nombre"], apellido=info["apellido"], mail=info["mail"], especialidad=info["especialidad"])

            cuidador.save()

            return render(request,"AppEntre2/inicio.html")

    else:

        form1 = Cuidadorform()

    return render(request, "AppEntre2/cuidadorform.html", {"form1":form1})


def busquedaReserva(request):

    return render(request, "AppEntre2/busquedaReserva.html")

def resultadoReservas(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        cant_especies = Reserva.objects.filter(nombre_icontains=nombre)
        ubicacion = Reserva.objects.filter(nombre_icontains=nombre)

        return render(request, "AppEntre2/resultadosreserva.html", {"nombre":nombre, "cant_especie":cant_especies, "ubicacion":ubicacion})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

