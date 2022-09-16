from django.db import models



# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    #Hay una herencia en estas clases, tomando la clase
    #de models importado de django.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregada = models.BooleanField()

class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    relación = models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()
    Edad = models.IntegerField()
