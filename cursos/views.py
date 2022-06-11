import pyrebase
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

config={
    "apiKey": "AIzaSyAojY9DDWrViFN4uAi-95ueJjB_XTE3eL4",
    "authDomain": "c-finder-7f032.firebaseapp.com",
    "databaseURL": "https://c-finder-7f032-default-rtdb.firebaseio.com",
    "projectId": "c-finder-7f032",
    "storageBucket": "c-finder-7f032.appspot.com",
    "messagingSenderId": "527727009170",
    "appId": "1:527727009170:web:3fc48042890f2fb861b54b"    
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
storage = firebase.storage()

# Create your views here.


def login(request):
    correo = request.POST.get('correo')
    contraseña = request.POST.get('contraseña')
    try:
        user = auth.sign_in_with_email_and_password(correo, contraseña)
        return redirect('cursos')
    except:
        print("Invalid user or password. Try again")
    return render(request, 'cursos/login.html')

def profesor(request):
    return render(request, 'cursos/v_profesor.html') 


def fpassword(request):
    return render(request, 'cursos/forgot_password.html') 


def cursos(request):
    return render(request, 'cursos/v_cursos.html')


def registro(request,id):
    correo = request.POST.get('correo')
    contraseña = request.POST.get('contraseña')
    conf_contraseña = request.POST.get('contraseñarep')
    try:
       user = auth.create_user_with_email_and_password(correo, contraseña)
    except:
        print("Error en la creacion de usuario")
    boleta = request.POST.get('NumBolet')
    nombre = request.POST.get('nombs')
    apellido_paterno = request.POST.get('appatern')
    apellido_materno = request.POST.get('apmatern')
    datos_alumno = {'correo': correo, 'contraseña': contraseña, 'conf_contraseña': conf_contraseña, 'nombre': nombre,
                    'apellido_materno': apellido_materno, 'apellido_paterno': apellido_paterno}
    database.child("alumno").push(datos_alumno)
    return render(request, 'cursos/registro_nu.html', {'id':id})
