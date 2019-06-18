from django.shortcuts import render, redirect, get_object_or_404
from .models import Sala
from .forms import SalaForm
from ..mapas.models import Mapa

def listar(request):
  salas = Sala.objects.all()
  return render(request, 'salas/listar.html', {'salas': salas})

def visualizar(request, id):
  sala = get_object_or_404(Sala, id = id)
  return render(request, 'salas/visualizar.html', {'sala': sala})

def cadastrar(request):
  if request.method == "POST":
    form = SalaForm(request.POST)
    if form.is_valid():
      sala = form.save(commit=False)
      local = Mapa.objects.create(nome = 'Mapa da Sala: ' + str(sala.numero), latitude = sala.latitude, longitude = sala.longitude)
      sala.local = local
      sala.save()
    return redirect('salas:listar')
  else:
    form = SalaForm()
    return render(request, 'salas/editar.html', {'form': form})

def editar(request, id):
  sala = get_object_or_404(Sala, id = id)
  if request.method == "POST":
    form = SalaForm(request.POST, instance = sala)
    if form.is_valid():
      form.save()
    return redirect('salas:listar')
  else:
    form = SalaForm(instance = sala)
    return render(request, 'salas/editar.html', {'form': form})

def remover(request, id):
  sala = get_object_or_404(Sala, id = id)
  sala.delete()
  return redirect('salas:listar')
