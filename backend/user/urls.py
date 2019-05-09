from django.urls import path
from django.contrib import admin
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.listar, name='listar'),
    path('<int:id>', views.visualizar, name = 'visualizar'),
    path('cadastrar', views.signup, name='cadastrar'),
    path('remover/<int:id>', views.remover, name='remover'),
]