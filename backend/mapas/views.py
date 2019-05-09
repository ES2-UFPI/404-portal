from django.shortcuts import render
from .models import Mapa

def listar(request):
	mapas = Mapa.objects.all()
	return render(request, 'mapas/listar.html', {'mapas': mapas})
