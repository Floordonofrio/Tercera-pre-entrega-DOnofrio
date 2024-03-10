from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('clases/', clases, name="clases"),
    path('profesores/', profesores, name="profesores"),
    path('alumnos/', alumnos, name="alumnos"),
    #-----------Formularios-------------------
    path('clases_form/', clasesForm, name="clases_form"),
    path('profesores_form/', profesoresForm, name="profesores_form"),
    path('alumnos_form/', alumnosForm, name="alumnos_form"),
    #------------Busqueda-----------------------
    path('buscar_clases/', buscarClases, name="buscar_clases"),
    path('encontrar_clases/', encontrarClases, name="encontrar_clases"),
    
]
