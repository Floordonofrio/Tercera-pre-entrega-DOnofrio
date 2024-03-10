from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render (request, "aplicacion/index.html")

def alumnos(request):
    contexto =  {'alumnos' : Alumnos.objects.all()}
    return render (request, "aplicacion/alumnos.html", contexto)

def clases(request):
    contexto =  {'clases' : Clases.objects.all()}
    return render (request, "aplicacion/clases.html", contexto)

def profesores(request):
    contexto =  {'profesores' : Profesores.objects.all()}
    return render (request, "aplicacion/profesores.html", contexto)

#---------Forms-----------
# Formulario Clases
def clasesForm(request):
    if request.method == "POST" :
        #Es la 2da o no vez que ingresa 
        miForm = ClasesForm(request.POST)
        if miForm.is_valid():
            clases_id = miForm.cleaned_data.get("id")    
            clases_nombre = miForm.cleaned_data.get("nombre")
            clases_profesor = miForm.cleaned_data.get("profesor")        
            clases = Clases(id = clases_id, nombre = clases_nombre, profesor = clases_profesor)
            clases.save()
            contexto =  {'clases' : Clases.objects.all()}
            return render (request, "aplicacion/clases.html", contexto)
    else:
        miForm = ClasesForm()
    return render(request, "aplicacion/clasesForm.html",{ "form" : miForm})
        
        
#Formulario profesores
def profesoresForm(request):
    if request.method == "POST" :
        #Es la 2da o no vez que ingresa 
        miForm = ProfesoresForm(request.POST)
        if miForm.is_valid():   
            profesores_nombre = miForm.cleaned_data.get("nombre")
            profesores_apellido = miForm.cleaned_data.get("apellido") 
            profesores_email = miForm.cleaned_data.get("email")               
            profesores = Profesores(nombre = profesores_nombre, apellido = profesores_apellido, email = profesores_email)
            profesores.save()
            contexto =  {'profesores' : Profesores.objects.all()}
            return render (request, "aplicacion/profesores.html", contexto)
    else:
        miForm = ProfesoresForm()
    return render(request, "aplicacion/profesoresForm.html",{ "form" : miForm})

#Formulario alumnos
def alumnosForm(request):
    if request.method == "POST" :
        #Es la 2da o no vez que ingresa 
        miForm = AlumnosForm(request.POST)
        if miForm.is_valid():   
            alumnos_nombre = miForm.cleaned_data.get("nombre")
            alumnos_apellido = miForm.cleaned_data.get("apellido") 
            alumnos_id= miForm.cleaned_data.get("id")
            alumnos_fichaMedica= miForm.cleaned_data.get("fichaMedica")       
            alumnos_entregaFicha= miForm.cleaned_data.get("entregaFicha")                                              
            alumnos = Alumnos(nombre = alumnos_nombre, apellido = alumnos_apellido, id = alumnos_id, fichaMedica = alumnos_fichaMedica, entregaFicha = alumnos_entregaFicha)
            alumnos.save()
            contexto =  {'alumnos' : Alumnos.objects.all()}
            return render (request, "aplicacion/alumnos.html", contexto)
    else:
        miForm = AlumnosForm()
    return render(request, "aplicacion/alumnosForm.html",{ "form" : miForm})


#Busqueda
def buscarClases(request):
    return render(request, "aplicaciones/buscar.html")

def encontrarClases(request):
    if request.GET ["buscar"]:
        patron = request.GET ["buscar"]
        clases = Clases.objects.filter(nombre__icontains=patron)
        contexto = {"clases" : clases}
        return render(request , "aplicacion/clases.html", contexto)
    
    
    contexto =  {'clases' : Clases.objects.all()}
    return render (request, "aplicacion/clases.html", contexto)
        