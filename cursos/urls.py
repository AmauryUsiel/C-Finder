from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('profesor/', views.profesor, name='profesor'),
    path('fpassword/', views.fpassword, name='fpassword'),
    path('registro/', views.registro, name='registro'),
    path('cursosdepython/', views.cpython, name='cursosdepython'),
    path('cursosdeandroidstudio/', views.candroid, name= 'cursosdeandroidstudio')
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
