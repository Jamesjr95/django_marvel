from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth import (
    get_user_model, # returns the AUTH_USER_MODEL variable's value from settings.py
    authenticate,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserAuthForm

def register(request):

    form = UserAuthForm()
    if request.method == 'GET':
        context = {
            'form': form
        }

        return render(request, 'users/register.html', context)
    if request.method == 'POST':
        # create a UserAuthForm with the data from the HTML form
        form = UserAuthForm(request.POST)

        # print(form.is_valid())
        # print(form.errors)

        if form.is_valid():
            # commit=False will create the object but won't save it
            new_user = form.save(commit=False)

            # set the new user's password
            # validated form data is in form.cleaned_data
            new_user.set_password(form.cleaned_data['password'])


            # save the object to the database
            new_user.save()

            # redirect() does the same thing as HttpResponseRedirect
            return redirect(reverse('users_app:register'))

        else:
            context = {
                'form': UserAuthForm(),
                'errors': [value for value in form.errors.values()]
            }

            return render(request, 'users/register.html', context)

