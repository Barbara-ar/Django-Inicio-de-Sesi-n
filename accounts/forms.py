from django import forms
from django.contrib.auth import get_user_model  # Obtiene el modelo de usuario
from django.contrib.auth.forms import UserCreationForm

# Formulario para el registro de nuevos usuarios
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # Usamos el modelo de usuario personalizado
        fields = ['email', 'username', 'age']  # Campos que el usuario podrá completar

# Formulario para editar el perfil del usuario
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()  # Usamos el modelo de usuario personalizado
        fields = ['username', 'email', 'first_name', 'last_name', 'age']  # Campos que el usuario podrá editar
