from django.urls import path
from AppCoder.views import *
#Las traigo todas, porque todas las funciones son públicas
#Es decir, no me interesa limitar el acceso para uso




urlpatterns = [
    path('', inicio),
    path('cursos/', cursos),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    path('profesores/', profesores),
    path('home/', home),
   
 
]