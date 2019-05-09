from django.urls import path
from . import views

app_name = 'reservas'
urlpatterns = [
    path('', views.listar, name='listar'),
    path('<int:id>', views.visualizar, name = 'visualizar'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('remover/<int:id>', views.remover, name='remover'),
    path('avaliar/<int:id>', views.avaliar, name='avaliar')
]