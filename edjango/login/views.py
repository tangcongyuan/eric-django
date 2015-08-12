from django.shortcuts import render, redirect
from django.contrib import auth
from login.forms import UserLoginForm

# Create your views here.

def login(request):
    loginForm = UserLoginForm()
    context = { 'loginForm': loginForm }
    return render(request, 'login.html', context)

def auth_view(request):
    loginForm = UserLoginForm(request.POST)
    if loginForm.is_valid():
        context = {}
        return redirect('/', context)
    else:
        print 'request not valid!'
        return redirect('user_login')
