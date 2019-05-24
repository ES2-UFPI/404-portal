from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import SignUpForm

def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('user:listar')
    else:
      form = SignUpForm()
  return render(request, 'usuarios/cadastrar.html', {'form': form})

# def login_(request):
#     pass

# def logout_(request):
#     pass

def listar(request):
  users = User.objects.all()
  return render(request, 'usuarios/listar.html', {'users': users})

def visualizar(request, id):
  user = get_object_or_404(User, id = id)
  return render(request, 'usuarios/visualizar.html', {'user': user})

def remover(request, id):
  user = get_object_or_404(User, id = id)
  user.delete()
  return redirect('user:listar')
