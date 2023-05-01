from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from account.forms import UserRegisterForm
from TApp import *

# def register_account(request):
#     if request.method == "POST":
#         # form = UserCreationForm(request.POST)
#         form = UserRegisterForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect("accountLogin")
#
#     # form = UserCreationForm()
#     form = UserRegisterForm()
#     context = {
#         "form": form
#     }
#     return render(request, "account/login.html", context=context)

def login_account(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            user = authenticate(username=informacion['username'], password=informacion['password'])
            if user:
                login(request, user)

                return redirect('hoy')
            else:
                return redirect("login")

    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "login.html", context=context)


def logout(request):
    return render("TApp/inicio.htlm")