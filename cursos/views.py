from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'cursos/login.html') 

def profesor(request):
    return render(request, 'cursos/v_profesor.html') 

def fpassword(request):
    return render(request, 'cursos/forgot_password.html') 

def cursos(request):
    return render(request, 'cursos/v_cursos.html') 