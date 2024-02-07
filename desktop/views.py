from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect('desktop:desktop')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('desktop:desktop')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('desktop:login')


@login_required(login_url='/login/')
def desktop_view(request):
    return render(request, 'desktop.html')

