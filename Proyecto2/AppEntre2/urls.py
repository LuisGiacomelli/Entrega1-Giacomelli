from django.urls import path
from AppEntre2.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path('reservas/', reserva, name="Reservas"),
    path('animales/', animal, name="Animales"),
    path('cuidadores/', cuidador, name="Cuidadores"),
    path('reservaform/', reservaform, name="Reservaform"),
    path('animalform/', animalform, name="Animalform"),
    path('cuidadorform/', cuidadorform, name="Cuidadorform"),
    path('buscarreserva/', busquedaReserva, name="BuscarReserva"),
    path('resultadoreserva/', resultadoReservas, name="ResultadosReservas"),
]
