from django.shortcuts import render, redirect
from django.contrib import auth
from accounts.forms import UserLoginForm

# Create your views here.

def login(request):
    loginForm = UserLoginForm()
    # Dealing with user authentication situation.
    if request.method == 'POST':
        loginForm = UserLoginForm(request.POST)
        context = { 'loginForm': loginForm }
        if loginForm.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('player_loggedIn')
            else:
                context['playerDoesNotExist'] = 'Please check your username and/or password.'
                return render(request, 'login.html', context)
        else:
            return render(request, 'login.html', context)
    
    else:
        context = { 'loginForm': loginForm }
        return render(request, 'login.html', context)
    
def logout(request):
    pass

def loggedIn(request):
    return render(request, 'loggedIn.html')