from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from Porfolio.models import experienciasModels, Avatar
from Porfolio.forms import registroFormularioExperiencia, UserRegisterForm, UserEditForm

from django.views.generic import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.urls import reverse_lazy


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



############################# VISTAS SIMPLES ###############################

@login_required
def Inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "Porfolio/Inicio.html",{"url": avatares[0].imagen.url})

def referencia(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'Porfolio/referencias.html',{"url": avatares[0].imagen.url})

def porfolio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'Porfolio/porfolio.html',{"url": avatares[0].imagen.url})

############################# VISTAS SIMPLES ###############################


#################### ADMINISTRAR #########################################

@login_required
def administracion_Vista(request):
    if request.method == 'POST':

            miFormulario = registroFormularioExperiencia(request.POST, files=request.FILES)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = experienciasModels (titulo=informacion['titulo'], año=informacion['año'], descripcion=informacion['descripcion'], imagen=informacion['imagen']) 
                  curso.save()
                  return render(request, "Porfolio/Inicio.html")
    else: 
        miFormulario= registroFormularioExperiencia()
    return render(request, "Porfolio/administrar.html", {"miFormulario":miFormulario})



############################# LEER ###############################
def leer_Experiencia(request):
      persona = experienciasModels.objects.all()
      contexto= {"persona":persona} 
      return render(request, "Porfolio/experiencia.html",contexto)

 ############################# LEER ###############################    
def buscar_Experiencia(request):
    if request.GET['titulo'] == '':
        return render (request, "Porfolio/administrar.html", {"mensaje": "Busqueda incorrecta, Debe ingresar datos"})
    else:
        if request.GET['titulo']:
            titulo = request.GET['titulo']
            titulo = experienciasModels.objects.filter(titulo__icontains=titulo)
            return render(request,"Porfolio/buscar.html",{"experiencia":titulo})
        else:
            respuesta = "<H1>No se encuentra</H1>"
        return render(request, "Porfolio/buscar.html")
        


def eliminar_Experiencia(request,experiencia_titulo):
    variable =experienciasModels.objects.get(titulo=experiencia_titulo)
    variable.delete()
    return render(request, "Porfolio/administrar.html", {"mensaje": "EXPERIENCIA ELIMINADA CON EXITO" })

def editar_Experiencia(request,experiencia_titulo):
    variable =experienciasModels.objects.get(titulo=experiencia_titulo)
    if request.method == 'POST':
        miFormulario = registroFormularioExperiencia(request.POST, files=request.FILES)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            variable.titulo = informacion['titulo']
            variable.año = informacion['año']
            variable.descripcion = informacion['descripcion']
            variable.imagen = informacion['imagen']
            variable.save()
            return render(request, "Porfolio/administrar.html", {"mensaje": "EXPERIENCIA EDITADA CON EXITO" })
    else:
        miFormulario = registroFormularioExperiencia(initial={'titulo' : variable.titulo, 'año' : variable.año, 'descripcion' : variable.descripcion, 'imagen' : variable.imagen})
    return render(request, "Porfolio/editarExperiencia.html", {"miFormulario":miFormulario, "experiencia_titulo":experiencia_titulo})

#################### ADMINISTRAR #########################################


#################### CLASES #########################################



class CursoList(LoginRequiredMixin, ListView):

      model = experienciasModels 
      template_name = "Porfolio/administrar.html"

#################### CLASES #########################################


#################### USUARIO #########################################
def login_request(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
                  mail = form.cleaned_data.get('mail')
                  user = authenticate(username = usuario , password = contra, mail_1 = mail)
                 
                  if user is not None:
                        login(request, user)

                        return render (request, "Porfolio/administrar.html", {"mensaje": f"Bienvenido/a {usuario}"})
                  else:
                       
                        return render (request, "Porfolio/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "Porfolio/inicio.html", {"mensaje":"Formulario erroneo"})
      form = AuthenticationForm()
    
      return render(request, "Porfolio/login.html", {'form': form})

def register(request):
      
      if request.method == "POST":

            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()

                  return render(request, "Porfolio/inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "Porfolio/registro.html", {"form": form})


@login_required
def editarPerfil(request):
      usuario = request.user
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
                  return render(request, "Porfolio/administrar.html")
      else:
            miFormulario = UserEditForm(initial={'email':usuario.email})
      return render(request, "Porfolio/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


#################### USUARIO #########################################

