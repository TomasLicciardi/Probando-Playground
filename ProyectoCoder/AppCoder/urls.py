from django.urls import path
from AppCoder.views import *

#Aca pongo todos los urls de la app en la que estoy

urlpatterns = [
    path('curso/', curso),
    path('cursos/', cursos),
    path('', inicio),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    path('profesores/', profesores),
]
