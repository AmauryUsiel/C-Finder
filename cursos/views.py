from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse 
from curso_display.models import Curso

# Create your views here.


def login(request): 
    return render(request, 'cursos/login.html')

def profesor(request):
    return render(request, 'cursos/v_profesor.html') 

def fpassword(request):
    return render(request, 'cursos/forgot_password.html') 


def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/v_cursos.html', {'cursos': cursos})
 
def registro(request):
    return render(request, 'cursos/registro_nu.html')  

def cpython(request):
    return render(request, 'cursos/cursosdepython.html') 

def candroid(request):
    return render(request, 'cursos/cursosdeandroidstudio.html')
