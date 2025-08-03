

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserProfileForm
from .models import PerfilUsuario 

class CustomLoginView(LoginView):
    
    template_name = 'registration/login.html'
    redirect_authenticated_user = True 

class CustomLogoutView(LogoutView):
    
    next_page = reverse_lazy('propiedades:index') 

def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            messages.success(request, f'Tu cuenta ha sido creada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('usuarios:login')
        else:
            messages.error(request, 'Error al registrar el usuario. Por favor, revisa los datos.')
    else:
        form = UserRegisterForm()
    return render(request, 'usuarios/register.html', {'form': form})

@login_required
def profile(request):
    """
    Vista de perfil del usuario.
    Requiere que el usuario esté autenticado.
    """
    try:
        perfil = request.user.perfilusuario
    except PerfilUsuario.DoesNotExist:
        
        perfil = PerfilUsuario.objects.create(user=request.user)

    context = {
        'user': request.user,
        'perfil': perfil,
    }
    return render(request, 'usuarios/profile.html', context)

@login_required
def profile_edit(request):
    
    try:
        perfil = request.user.perfilusuario
    except PerfilUsuario.DoesNotExist:
        perfil = PerfilUsuario.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('usuarios:profile')
        else:
            messages.error(request, 'Error al actualizar el perfil. Por favor, revisa los datos.')
    else:
        form = UserProfileForm(instance=perfil)
    return render(request, 'usuarios/profile_edit.html', {'form': form})

