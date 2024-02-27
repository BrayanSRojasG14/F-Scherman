from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Fundacion.")

def login(request):
    return HttpResponse("Iniciar sesion.")

