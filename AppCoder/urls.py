from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('clases/', clases, name="clases"),
    path('profesores/', profesores, name="profesores"),
    path('alumnos/', alumnos, name="alumnos"),
    
]
