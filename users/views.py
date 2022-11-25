from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import unauthenticated_user
from .forms import UserRegistrationForm, UserUpdateForm
from django.views.generic import (
    DeleteView,
    UpdateView
)
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  # Restrict user access
from django.contrib.messages.views import SuccessMessageMixin


@unauthenticated_user
def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'wrong details, try again!')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')


@unauthenticated_user
def registration(request):
    context = {
        'title': 'signup',
        'form': ''
    }

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='admin')
            user.groups.add(group)
            username = form.cleaned_data.get('username')

            messages.success(
                request, f'{username} Account created successfully, you can now login!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        context['form'] = form

    return render(request, 'registration/register.html', context)


def logout_view(request):
    logout(request)
    messages.success(
        request, f'You were successfully, logged out!')
    return redirect('login')


def change_password(request):
    return render(request, 'registration/forgot-password.html')


def user_profile(request):
    return render(request, 'registration/profile.html')


class UsersUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'last_name', 'first_name']
    success_url = reverse_lazy('home')
    success_message = 'Patient updated successfully!'


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy('home')
    success_message = 'User deleted successfully!'
