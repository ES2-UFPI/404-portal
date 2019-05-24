from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm

def listar(request):
  eventos = Evento.objects.all().order_by('-data_criacao')
  return render(request, 'eventos/listar.html', {'eventos': eventos})

def visualizar(request, id):
  evento = get_object_or_404(Evento, id = id)
  return render(request, 'eventos/visualizar.html', {'evento': evento})

def cadastrar(request):
  if request.method == "POST":
    form = EventoForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('eventos:listar')
  else:
    form = EventoForm()
    return render(request, 'eventos/editar.html', {'form': form})

def editar(request, id):
  evento = get_object_or_404(Evento, id = id)
  if request.method == "POST":
    form = EventoForm(request.POST, instance = evento)
    if form.is_valid():
      form.save()
    return redirect('eventos:listar')
  else:
    form = EventoForm(instance = evento)
    return render(request, 'eventos/editar.html', {'form': form})

def remover(request, id):
  evento = get_object_or_404(Evento, id = id)
  evento.delete()
  return redirect('eventos:listar')
