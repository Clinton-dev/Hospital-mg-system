from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm


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


def registration(request):
    context = {
        'title': 'signup',
        'form': ''
    }

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created successfully, you can now login!')
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
