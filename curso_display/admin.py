from django.contrib import admin
from .models import Curso

# Register your models here.

#asi registtramos el servicio 

class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #para que sean solo de lectura

admin.site.register(Curso, CursoAdmin) #Aqui registramos el modelo Curso con el admin