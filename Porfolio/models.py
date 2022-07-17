from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField

# Create your models here.

class experienciasModels(models.Model):
    titulo = models.CharField(max_length=100)
    año = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to="media/images/")
    def __str__(self):
        return f"Titulo: {self.titulo} - Año {self.año}  - Descripcion  {self.descripcion} "


class referenciaModels(models.Model):
    nombre = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=100)
    imagen = models.CharField(max_length=100)
    def __str__(self):
        return f"Nombre: {self.nombre} - Oupacion {self.ocupacion}  - Linkedin  {self.linkedin} "

class porfolioModels(models.Model):
    nombre = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=100)
    imagen = models.CharField(max_length=100)
    def __str__(self):
        return f"Nombre: {self.nombre} - Oupacion {self.ocupacion}  - Linkedin  {self.linkedin} "


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)