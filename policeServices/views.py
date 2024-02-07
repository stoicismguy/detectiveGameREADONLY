from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required(login_url='/sex/')
def main_view(request):
    return render(request, "base.html")
