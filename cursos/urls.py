from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('profesor/', views.profesor, name='profesor'),
    path('fpassword/', views.fpassword, name='fpassword'),
    path('cursos/', views.cursos, name='cursos'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
