from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    
    def __str__(self):
        return self.nombre + " Comision: " + str(self.comision)

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre +" " + self.apellido + " " + str(self.fecha_nacimiento)

class Entregado(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    estado = models.BooleanField()

    def __str__(self):
        return f"Entrega dia: {self.fecha}"