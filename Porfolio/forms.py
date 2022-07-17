from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class registroFormularioExperiencia(forms.Form):
    titulo = forms.CharField(max_length=100)
    año = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=1000)
    imagen = forms.ImageField()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        print(model)
        fields = ['username', 'password1', 'password2', 'email']
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar Email')
    password1 = forms.CharField(label='Pass', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita Pass', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}
