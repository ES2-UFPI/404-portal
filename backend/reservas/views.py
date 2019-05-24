from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm, AvaliarReservaForm

def listar(request):
  reservas = Reserva.objects.all()
  return render(request, 'reservas/listar.html', {'reservas':reservas})

def visualizar(request, id):
  reserva = get_object_or_404(Reserva, id = id)
  return render(request, 'reservas/visualizar.html', {'reserva': reserva})

def cadastrar(request):
  if request.method == "POST":
    form = ReservaForm(request.POST)
    if form.is_valid():
      reserva = form.save(commit=False)
      reserva.solicitante = request.user
      reserva.save()
    return redirect('reservas:listar')
  else:
    form = ReservaForm()
    return render(request, 'reservas/editar.html', {'form': form})

def editar(request, id):
  reserva = get_object_or_404(Reserva, id = id)
  if request.method == "POST":
    form = ReservaForm(request.POST, instance = reserva)
    if form.is_valid():
      form.save()
    return redirect('reservas:listar')
  else:
    form = ReservaForm(instance = reserva)
    return render(request, 'reservas/editar.html', {'form': form})

def remover(request, id):
  reserva = get_object_or_404(Reserva, id = id)
  reserva.delete()
  return redirect('reservas:listar')

def avaliar(request, id):
  reserva = get_object_or_404(Reserva, id = id)
  if request.method == "POST":
    form = AvaliarReservaForm(request.POST, instance = reserva)
    if form.is_valid():
      reserva = form.save(commit=False)
      reserva.avaliada_por = request.user
      reserva.avaliada = True
      reserva.save()
    return redirect('reservas:listar')
  else:
    form = AvaliarReservaForm(instance = reserva)
    return render(request, 'reservas/avaliar.html', {'form': form})
