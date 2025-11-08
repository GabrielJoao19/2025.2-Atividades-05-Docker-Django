from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Olá! Bem-vindo à aplicação Django em Docker!")