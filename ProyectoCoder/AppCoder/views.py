from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *
# Create your views here.

def curso(request):
    curso2 = Curso(nombre = "Django", comision = 1234)
    curso2.save()
    texto = f"Curso creado: {curso2.nombre} y comision {curso2.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    if (request.method) == "POST":
       form = CursoForm(request.POST)
       if form.is_valid():
        info = form.cleaned_data
        nombre = info['nombre']
        comision = info['comision']
        curso = Curso(nombre = nombre, comision = comision)
        curso.save()
        return render(request, "AppCoder/inicio.html")
    else:
        form = CursoForm()
        return render(request,"AppCoder/cursos.html", {"curso_formulario": form})

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def padre(request):
    return render(request, "AppCoder/padre.html")

'''def curso_formulario(request):

    if (request.method) == "POST":
        nombre = request.POST.get("curso")
        comision = request.POST.get("comision")
        curso = Curso(nombre = nombre, comision = comision)
        curso.save()
        return render(request, "AppCoder/inicio.html") #Si se guardo bien nos deberia enviar al inicio!
    
    return render(request, "AppCoder/formulario.html")  VISTA PARA FORMULARIO HTML'''

def profe_formulario(request):

    if (request.method) == "POST":
        form = ProfeForm(request.POST)
        print("Entra a la funcion")
        if form.is_valid():
            print("Entra al if")
            info = form.cleaned_data
            #nombre = info['nombre']
            #apellido = info['apellido']
            #email = info['email']
            #nacimiento = info['fecha_nacimiento']
            profesor = Profesor(nombre = info['nombre'], apellido = info['apellido'], email = info['email'], fecha_nacimiento = info['fecha_nacimiento'])
            profesor.save()
            return render(request,"AppCoder/inicio.html")
    else:
        print("Entra al else")
        form = ProfeForm()
        return render(request,"AppCoder/profe_formulario.html", {"profe_formulario": form})

def busqueda_comision(request):
    return render(request, "AppCoder/busqueda_comision.html")

def buscar(request):
    if request.GET["comision"]:
        comision = request.GET["comision"]
        cursos = Curso.objects.filter(comision=comision)
        return render(request, "AppCoder/resultado_busqueda.html", {"cursos": cursos})
    else:
        return render(request, "AppCoder/busqueda_comision.html", {"error": "Ha ocurrido un error!!!"})