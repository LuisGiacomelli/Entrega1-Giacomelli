from django import forms

class Animalform(forms.Form):

    especie = forms.CharField()
    cant = forms.IntegerField()
    reserva = forms.CharField()


class Cuidadorform(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()
    especialidad = forms.CharField()

class Reservaform(forms.Form):
    nombre = forms.CharField()
    cant_especies = forms.IntegerField()
    ubicacion = forms.CharField()

