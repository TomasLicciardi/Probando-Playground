from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.

def curso(request):
    curso2 = Curso(nombre = "Django", comision = 1234)
    curso2.save()
    texto = f"Curso creado: {curso2.nombre} y comision {curso2.comision}"
    return HttpResponse(texto)
    