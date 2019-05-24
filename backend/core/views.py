from django.shortcuts import render, redirect, get_object_or_404
from .models import Portal
from .forms import PortalForm

def home(request):
  portal = Portal.objects.all().first()
  context = {
    "portal": portal
  }
  return render(request, 'index.html', context)

def listar(request):
  portais = Portal.objects.all()
  return render(request, 'core/listar.html', {'portais': portais})

def visualizar(request, id):
  portal = get_object_or_404(Portal, id = id)
  return render(request, 'core/visualizar.html', {'portal': portal})

def editar(request, id):
  portal = get_object_or_404(Portal, id = id)
  if request.method == "POST":
    form = PortalForm(request.POST, instance = portal)
    if form.is_valid():
      form.save()
      return redirect('core:listar')
  else:
    form = PortalForm(instance = portal)
  return render(request, 'core/editar.html', {'form': form})
