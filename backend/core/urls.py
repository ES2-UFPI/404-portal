from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
  path('', views.home, name='home'),
  path('<int:id>', views.visualizar, name = 'visualizar'),
  path('listar/', views.listar, name='listar'),
  path('portal/editar/<int:id>', views.editar, name='editar'),
]
