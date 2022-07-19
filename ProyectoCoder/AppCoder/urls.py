from unicodedata import name
from django.urls import path
from AppCoder.views import *

#Aca pongo todos los urls de la app en la que estoy

urlpatterns = [
    path('curso/', curso, name="curso"),
    path('cursos/', cursos, name="cursos"),
    path('', inicio, name="inicio"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
    path('profesores/', profesores, name="profesores"),
    path('profe_formulario/', profe_formulario, name="profe_formulario"),
    path('busqueda_comision/', busqueda_comision, name="busqueda_comision"),
    path('buscar/', buscar, name="buscar"),
]
