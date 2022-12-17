from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registrar_User(UserCreationForm):
    name = forms.CharField(max_length=25, label="Nombre")
    username = forms.CharField(max_length=30, label="Username")
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ["name", "email","username", "password1", "password2"]

class UserEditForm(UserCreationForm):
    first_name = forms.CharField(max_length=25, label="Editar nombre")
    email = forms.EmailField(label="Editar correo electrónico")
    password1 = forms.CharField(label="Editar contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar la contraseña", widget=forms.PasswordInput, required=False)

    class Meta: 
        model = User
        fields = ["first_name", "email","password1", "password2"]
        exclude = ["username"]
        help_texts = {"first_name": "","email": "Indica un correo que utilices habitualmente"}

class AvatarForm(forms.Form):
    imagen = forms.ImageField()
