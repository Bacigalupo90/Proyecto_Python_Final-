

from django import forms
from .models import Propiedad

class PropiedadForm(forms.ModelForm):
    
    class Meta:
        model = Propiedad
        fields = ['titulo', 'descripcion', 'precio', 'imagen', 'fecha_publicacion']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}), 
        }

class PropiedadSearchForm(forms.Form):
   
    query = forms.CharField(max_length=100, required=False, label="Buscar Propiedad")

