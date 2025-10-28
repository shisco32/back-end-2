from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'nota1', 'nota2', 'nota3', 'fecha_ingreso', 'carrera']
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
        }