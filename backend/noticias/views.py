from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia
from .forms import NoticiaForm

def listar(request):
  noticias = Noticia.objects.all().order_by('-data_criacao')
  return render(request, 'noticias/listar.html', {'noticias': noticias})

def visualizar(request, id):
  noticia = get_object_or_404(Noticia, id = id)
  return render(request, 'noticias/visualizar.html', {'noticia': noticia})

def cadastrar(request):
  if request.method == "POST":
    form = NoticiaForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('noticias:listar')
  else:
    form = NoticiaForm()
    return render(request, 'noticias/editar.html', {'form': form})

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

def remover(request, id):
  noticia = get_object_or_404(Noticia, id = id)
  noticia.delete()
  return redirect('noticias:listar')
