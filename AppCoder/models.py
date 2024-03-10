from django.db import models

# Create your models here.

class Clases(models.Model):
    nombre =models.CharField(max_length=40)
    profesor = models.CharField(max_length=40)
    id = models.IntegerField(primary_key=True)
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Clase"
        verbose_name_plural = "Clases"
    
    def __str__(self):
        return f"{self.id}, {self.nombre}"

class Profesores(models.Model):
    nombre =models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
    class Meta:
        ordering = ["nombre"]
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Alumnos(models.Model):
    nombre =models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    fichaMedica = models.BooleanField()
    entregaFicha = models.DateField()
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
    
    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.apellido}"
    