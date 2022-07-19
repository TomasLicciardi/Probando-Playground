from django.contrib import admin
from .models import Curso, Entregado, Alumno, Profesor 
# Register your models here.

admin.site.register(Curso)
admin.site.register(Entregado)
admin.site.register(Alumno)
admin.site.register(Profesor)