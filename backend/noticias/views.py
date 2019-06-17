from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Noticia
from .forms import NoticiaForm
from backend.usuarios.models import Pessoa

def listar(request):
  pessoa = None
  if request.user.is_authenticated:
    user = request.user
    pessoa = Pessoa.objects.get(user=user)
  noticias = Noticia.objects.all().order_by('-data_criacao')
  return render(request, 'noticias/listar.html', {'noticias': noticias, 'pessoa': pessoa})

def visualizar(request, id):
  noticia = get_object_or_404(Noticia, id = id)
  return render(request, 'noticias/visualizar.html', {'noticia': noticia})

@login_required
def cadastrar(request):
  if request.method == "POST":
    form = NoticiaForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('noticias:listar')
  else:
    form = NoticiaForm()
    return render(request, 'noticias/editar.html', {'form': form})

@login_required
def editar(request, id):
  noticia = get_object_or_404(Noticia, id = id)
  if request.method == "POST":
    form = NoticiaForm(request.POST, instance = noticia)
    if form.is_valid():
      form.save()
    return redirect('noticias:listar')
  else:
    form = NoticiaForm(instance = noticia)
    return render(request, 'noticias/editar.html', {'form': form})

@login_required
def remover(request, id):
  noticia = get_object_or_404(Noticia, id = id)
  noticia.delete()
  return redirect('noticias:listar')
