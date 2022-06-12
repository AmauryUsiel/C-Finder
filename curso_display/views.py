from django.shortcuts import render

from curso_display.models import Curso
# Create your views here.

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos_display/v_cursos.html', {'cursos': cursos})