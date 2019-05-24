from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio
from .forms import LaboratorioForm

def listar(request):
  laboratorios = Laboratorio.objects.all()
  return render(request, 'laboratorios/listar.html', {'laboratorios': laboratorios})

def visualizar(request, id):
  laboratorio = get_object_or_404(Laboratorio, id = id)
  return render(request, 'laboratorios/visualizar.html', {'laboratorio': laboratorio})

def cadastrar(request):
  if request.method == "POST":
    form = LaboratorioForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('laboratorios:listar')
  else:
    form = LaboratorioForm()
    return render(request, 'laboratorios/editar.html', {'form': form})

def editar(request, id):
  laboratorio = get_object_or_404(Laboratorio, id = id)
  if request.method == "POST":
    form = LaboratorioForm(request.POST, instance = laboratorio)
    if form.is_valid():
      form.save()
    return redirect('laboratorios:listar')
  else:
    form = LaboratorioForm(instance = laboratorio)
    return render(request, 'laboratorios/editar.html', {'form': form})

def remover(request, id):
  laboratorio = get_object_or_404(Laboratorio, id = id)
  laboratorio.delete()
  return redirect('laboratorios:listar')
