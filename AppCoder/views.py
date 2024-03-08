from django.shortcuts import render
from .models import*

# Create your views here.
def home(request):
    return render (request, "aplicacion/index.html")

def alumnos(request):
    return render (request, "aplicacion/alumnos.html")

def clases(request):
    return render (request, "aplicacion/clases.html")

def profesores(request):
    contexto =  {'profesores' : Profesores.objects.all()}
    return render (request, "aplicacion/profesores.html", contexto)