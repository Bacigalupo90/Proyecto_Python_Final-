

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PerfilUsuario

class UserRegisterForm(UserCreationForm):
    """
    Formulario para el registro de nuevos usuarios.
    Extiende UserCreationForm para incluir email.
    """
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ["username", "email"] 

class UserProfileForm(forms.ModelForm):
    
    first_name = forms.CharField(label="Nombre", max_length=150, required=False)
    last_name = forms.CharField(label="Apellido", max_length=150, required=False)
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = PerfilUsuario
        fields = ['avatar', 'biografia'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return super().save(commit=commit)