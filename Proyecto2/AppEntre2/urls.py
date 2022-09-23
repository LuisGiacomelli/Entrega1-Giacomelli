from django.urls import path
from AppEntre2.views import *

urlpatterns = [
    path("", inicio),
    path('reservas/', reserva),
    path('animales/', animal),
    path('cuidadores/', cuidador),
]
