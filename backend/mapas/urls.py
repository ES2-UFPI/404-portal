from django.urls import path
from . import views

app_name = 'mapas'
urlpatterns = [
    path('', views.listar, name='listar'),
]