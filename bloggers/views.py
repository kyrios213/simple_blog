from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import PasswordsChangeForm, SignUpForm, EditProfileForm
from django.contrib.auth.views import PasswordChangeView


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('myblog:home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    success_url = reverse_lazy('bloggers:edit_profile')