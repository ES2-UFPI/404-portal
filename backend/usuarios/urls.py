from django.urls import path
from django.contrib import admin
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.listar, name='listar'),
    path('<int:id>', views.perfil, name = 'perfil'),
    path('cadastrar', views.signup, name='cadastrar'),
]