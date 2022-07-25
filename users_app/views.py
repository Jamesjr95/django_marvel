from django.shortcuts import render

from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth import (
    get_user_model,
    authenticate,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserAuthForm
from library_app.models import Checkout

#sign up view
def register(request):
    form = UserAuthForm()
    if request.method == 'GET':
        context = {
            'form': form
        }
        return render(request, 'users/register.html', context)
    if request.method == 'POST':
        form = UserAuthForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            checkout = Checkout.objects.create(owner=new_user)
            return redirect(reverse('users_app:register'))
        else:
            context = {
                'form': UserAuthForm(),
                'errors': [value for value in form.errors.values()]
            }

            return render(request, 'users/register.html', context)

#login view
def login(request):
    if request.method == 'GET':
        form = UserAuthForm()
        return render(request, 'users/login.html', {'form': form})
    elif request.method == 'POST':
        form = request.POST
        username = form['username']
        password = form['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'form': UserAuthForm(),
                'errors': ['Invalid Username or Password']
            }
            return render(request, 'users/login.html', context)
        else:
            django_login(request, user)
            return redirect(reverse('users_app:profile', kwargs={'username': user.username}))

#detail profile view
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    return render(request, 'users/profile.html', {'user': user})

#logout view
def logout(request):
    django_logout(request)

    return redirect(reverse('users_app:login'))