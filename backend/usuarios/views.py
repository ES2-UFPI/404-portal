from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import PessoaForm
from .models import Pessoa

def signup(request):
  form_pessoa = PessoaForm(request.POST, request.FILES)
  form_user = UserCreationForm(request.POST)

  # Mensagens de Erro e Sucesso
  mensagem = None

  if request.method == "POST":
    aluno = form_pessoa
    user = form_user

    if user.is_valid():
      user = user.save(commit=False)
      if aluno.is_valid():
        aluno = aluno.save(commit=False)
        # Desativando o usuário até que seja avaliado
        user.is_active = False
        user.save()
        # Relacionando a Pessoa com seu usuário
        aluno.user = user
        aluno.save()

        mensagem = "Usuário cadastrado com sucesso. Aguarde avaliação dos Coordenadores."

        return render(request, 'index.html', {'mensagem': mensagem})
    else:
      mensagem = "Erro ao cadastrar usuário. Tente novamente."

  return render(request, 'usuarios/cadastrar.html', {'form_user': form_user, 'form_pessoa':form_pessoa, 'mensagem':mensagem})

def listar(request):
  users = User.objects.all()
  return render(request, 'usuarios/listar.html', {'users': users})

def perfil(request, id):
  user = get_object_or_404(User, id = id)
  pessoa = get_object_or_404(Pessoa, user=user)
  return render(request, 'usuarios/perfil.html', {'pessoa': pessoa})

def remover(request, id):
  user = get_object_or_404(User, id = id)
  user.delete()
  return redirect('user:listar')
