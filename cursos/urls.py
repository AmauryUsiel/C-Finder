from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('profesor/', views.profesor, name='profesor'),
    path('fpassword/', views.fpassword, name='fpassword'),
]
