from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sign_in")
    else:
        form = RegistrationForm()
        
    return render(request, "app/register.html",{ "form":form, "heading":"Register Page" })


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["username"]
            user_pass = form.cleaned_data["password"]
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                login(request,user)
                messages.success(request, "Logged In Successfully")
                return redirect("profile")
            else:
                messages.info(request, "Enter valid user and password")
    else:
        form = AuthenticationForm()
    return render(request, "app/register.html", { "form":form, "heading":"Sign In Page" })


def sign_out(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect("home")


@login_required
def profile(request):
    return render(request, "app/profile.html")


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect("sign_in")
    else:
       form = PasswordChangeForm(request.user)
        
    return render(request, "app/register.html",{ "form":form, "heading":"Change password using old password" })


@login_required
def set_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect("sign_in")
    else:
       form = SetPasswordForm(request.user)
        
    return render(request, "app/register.html",{ "form":form, "heading":"Change password directly" })