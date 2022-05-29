from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'cursos/login.html') 

def profesor(request):
    return render(request, 'cursos/v_profesor.html') 