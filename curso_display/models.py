from django.db import models

# Create your models here.
class Curso(models.Model):
    titulo = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to='curso_display')
    nombrePlataforma = models.CharField(max_length=50, blank=True)
    enlace = models.URLField(max_length=200 , blank=True)
    description_vid = models.TextField(max_length=200 , blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        
    def __str__(self):
        return self.titulo