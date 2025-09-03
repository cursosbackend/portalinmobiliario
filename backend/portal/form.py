from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ["nro_region","nombre"]



class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ["region", "nombre"]


class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            "nombre",
            "descripcion",
            "imagen",
            "m2_construidos",
            "m2_totales",
            "estacionamientos",
            "habitaciones",
            "banos",
            "direccion",
            "precio_mensual",
            "comuna",
            "tipo_de_inmueble",
        ]


class SolicitudArriendoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = ["mensaje"]

class PerfilUserForm(forms.ModelForm):
    class Meta:
        model = PerfilUser
        fields = ["tipo_usuario", "rut", "password"] 




class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = PerfilUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "rut",
            "imagen",
            "tipo_usuario",
            "password1",
            "password2",
        ]

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
