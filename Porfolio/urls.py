from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('referencia', views.referencia, name='referencia'),
    path('porfolio', views.porfolio, name='porfolio'),


    path('administrar', views.administracion_Vista, name='administrar'),
    path('leerExperiencia', views.leer_Experiencia, name = "leerExperiencia"),
    path('buscar/', views.buscar_Experiencia),
    path('buscar/buscar/', views.buscar_Experiencia),
    path('eliminarExperiencia/<experiencia_titulo>/', views.eliminar_Experiencia, name="eliminarExperiencia"),
    path('editarExperiencia/<experiencia_titulo>/', views.editar_Experiencia, name="editarExperiencia"),




    #path('login', views.login_request, name='login'),
    #path('register', views.register, name='register'),
    #path('logout', LogoutView.as_view(template_name='Porfolio/logout.html'), name='logout'),



    path('administrar', views.CursoList.as_view(), name='administrar'),
    #path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    #path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    #path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    #path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    #path('login', views.login_request, name='login')

    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='Porfolio/inicio.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
]
