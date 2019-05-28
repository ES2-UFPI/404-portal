from django.shortcuts import render
from ..salas.models import Sala

def listar(request):
	salas = Sala.objects.all()
	return render(request, 'mapas/listar.html', {'salas': salas})