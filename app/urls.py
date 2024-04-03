from django.urls import path
from . import views

urlpatterns = [
    path('animales', views.animales, name='animales'),
    path('armas', views.armas, name='armas'),
    path('construcciones', views.construcciones, name='construcciones'),
    path('consumibles', views.consumibles, name='consumibles'),
    path('enemigos', views.enemigos, name='enemigos'),
    path('flora', views.flora, name='flora'),
    path('foro', views.forowiki, name='foro'),
    path('historia', views.historia, name='historia'),
    path('inicio-sesion', views.inicioSesion, name='inicio sesion'),
    path('logros', views.logros, name='logros'),
    path('lugares', views.menuPrincipal, name='lugares'),
    path('', views.menuPrincipal, name='home'),
    path('cuenta', views.miCuenta, name='cuenta'),
    path('recuperar-contrasena', views.recuperarContraseña, name='recuperar contrasena'),
    path('registro', views.registro, name='registro'),
]