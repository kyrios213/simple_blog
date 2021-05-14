from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView
from django.contrib.auth import views as auth_views

app_name = 'bloggers'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name='change_pass'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
]