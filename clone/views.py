from django.shortcuts import render
from .forms import UserRegister, UserLogin
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, logout

# Create your views here.

def main_page(request):
    return render(request, 'clone/mainPage.html')

def site_reg(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration was Satisfied')
            return redirect('login')
        else:
            messages.error(request, 'Your Form is not Valid, or SMT goes Wrong!')
    else:
        form = UserRegister()
    return render(request, 'clone/register.html', {'form': form})


    return render(request, 'clone/')

def site_login(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = UserLogin()

    return render(request, 'clone/login.html', {'form': form})

def site_logout(request):
    logout(request)
    return redirect('login')