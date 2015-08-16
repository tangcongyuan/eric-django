from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm

# Create your views here.

def login(request):
    loginForm = UserLoginForm()
    # Dealing with user authentication situation.
    if request.method == 'POST':
        loginForm = UserLoginForm(request.POST)
        context = { 'loginForm': loginForm }
        #print request.session.modified # False
        if loginForm.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            #print request.session.modified # False
            if user is not None:
                auth.login(request, user)
                #print request.session.modified # True
                request.session.set_expiry(10)
                #print request.session.modified # True
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
    
@login_required
def loggedIn(request):
    print request.is_ajax()
    return render(request, 'loggedIn.html')