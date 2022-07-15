from re import template
from xml.dom.minidom import Document
from django.http import HttpResponse
import datetime
from django.template import Context, Template,loader

def saludar(request):
    return HttpResponse("Hola Mundo")

def segunda_vista(request):
    return HttpResponse("Esto es easy,peasy")

def fecha_de_hoy(request):
    dia = datetime.datetime.today()
    cadena = f"<h1> Hoy es: {str(dia)} </h1>"
    return HttpResponse(cadena)

def anio_nacimiento(request):
    anio = datetime.datetime.now().year

def anio_nacimiento(request, edad):
    return HttpResponse("<h1>Tu año de nacimiento es: "+str(int(datetime.datetime.now().year)-int(edad))+"</h1>")    

def saludo_con_nombre(request, nombre):
    respuesta = "<h3> Hola, mi nombre es: "+ nombre + "<br>un gusto </h3>"
    diccionario = {'respuesta': respuesta}
    plantilla = loader.get_template('template.html')
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)

def probando_html(request):
    
    
    nom = "Tomas"
    ape = "Licciardi"
    
    lista_notas = [1,2,3,4,5,6,8,7,9]
    
    deporte = {"futbol": 500, "rugby": 1000, "tenis": 200}
    
    diccionario = {"nombre": nom, "apellido": ape,"lista": lista_notas, "deporte": deporte}
    
    plantilla = loader.get_template('template.html')
    
    
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)