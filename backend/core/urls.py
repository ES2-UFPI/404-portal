from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'
urlpatterns = [
  path('', views.home, name='home'),
  path('<int:id>', views.visualizar, name = 'visualizar'),
  path('listar/', views.listar, name='listar'),
  path('portal/editar/<int:id>', views.editar, name='editar'),
  path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name="login"),
  path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name="logout"),
]
