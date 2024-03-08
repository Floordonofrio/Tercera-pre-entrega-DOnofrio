from django.db import models

# Create your models here.

class Clases(models.Model):
    nombre =models.CharField(max_length=40)
    profesor = models.CharField(max_length=40)
    id = models.IntegerField

class Profesores(models.Model):
    nombre =models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    clase = models.IntegerField
    email = models.EmailField()

class Alumnos(models.Model):
    nombre =models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    id = models.IntegerField
    email = models.EmailField()
    fichaMedica = models.BooleanField()
    entregaFicha = models.DateField()
    