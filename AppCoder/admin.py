from django.contrib import admin

# Register your models here.
from .models import *


class ClasesAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")

class AlumnosAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "apellido")
    
class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email")
    
admin.site.register(Clases, ClasesAdmin)
admin.site.register(Alumnos, AlumnosAdmin)
admin.site.register(Profesores, ProfesoresAdmin)