from django import forms

class ClasesForm(forms.Form):
    id = forms.IntegerField(required=True)
    nombre = forms.CharField(max_length = 40, required= True)
    profesor = forms.CharField(max_length = 40, required= True)
    
class ProfesoresForm(forms.Form):
    nombre =forms.CharField(max_length=40, required= True)
    apellido = forms.CharField(max_length=40, required= True)
    email = forms.EmailField(required= True)
    
class AlumnosForm(forms.Form):
    nombre = forms.CharField(max_length=40, required= True)
    apellido = forms.CharField(max_length=40, required= True)
    id = forms.IntegerField(required= True)
    email = forms.EmailField(required= True)
    fichaMedica = forms.BooleanField(required= True)
    entregaFicha = forms.DateField(required= True)
    