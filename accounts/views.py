from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm, EditProfileForm  # Asegúrate de importar el formulario de edición
from .models import CustomUser

# Vista para el registro de usuarios
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Crea al usuario
            login(request, user)  # Inicia sesión al registrar
            messages.success(request, '¡Tu cuenta ha sido creada con éxito!')
            return redirect('accounts:account_details')  # Redirige a los detalles del usuario
    else:
        form = CustomUserCreationForm()  # Formulario vacío al cargar la página
    return render(request, 'accounts/signup.html', {'form': form})

# Vista para mostrar los detalles del usuario
@login_required
def account_details(request):
    return render(request, 'accounts/user_detail.html', {'user': request.user})

# Vista para editar el perfil del usuario
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)  # Rellena el formulario con los datos actuales del usuario
        if form.is_valid():
            form.save()  # Guarda los cambios
            messages.success(request, '¡Perfil actualizado con éxito!')
            return redirect('accounts:account_details')  # Redirige a los detalles del usuario
    else:
        form = EditProfileForm(instance=request.user)  # Muestra el formulario con los datos actuales del usuario

    return render(request, 'accounts/user_edit.html', {'form': form})  # Renderiza el formulario de edición

# Vista para eliminar la cuenta del usuario
@login_required
def delete_account(request):
    user = request.user
    if request.method == "POST":
        # Elimina la cuenta
        user.delete()
        messages.success(request, 'Tu cuenta ha sido eliminada con éxito.')
        return redirect('accounts:login')  # Redirige al login después de eliminar la cuenta
    return render(request, 'accounts/user_delete.html', {'user': user})  # Muestra una página de confirmación
