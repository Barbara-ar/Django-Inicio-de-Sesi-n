from django.urls import path
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación de Django
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('details/', views.account_details, name='account_details'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('delete_account/', views.delete_account, name='delete_account'),  # Agregar esta línea
]
