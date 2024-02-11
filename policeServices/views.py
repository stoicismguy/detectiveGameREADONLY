from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required(login_url='/sex/')
def database_view(request):
    input_selected = request.GET.get("input")
    context = {"input_selected": input_selected}
    return render(request, "base.html", context=context)


def signature_view(request):
    input_selected = request.GET.get("input")
    context = {"input_selected": input_selected}
    return render(request, "signature.html", context=context)


def search_view(request):
    return HttpResponse("asdggfgdfgdfgdfg")
