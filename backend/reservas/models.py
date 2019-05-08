from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from backend.laboratorios.models import Laboratorio
from backend.salas.models import Sala


class Reserva(models.Model):
    justificativa = models.TextField()
    data_hora_reserva = models.DateTimeField(null=True)
    data_hora_criacao = models.DateTimeField(default=timezone.now)
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, blank=True,null=True, related_name='+')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, null=True, blank=True,related_name='+')
    avaliada_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    avaliada = models.BooleanField(default=False)
    aceita = models.BooleanField(default=False)
    comentario = models.TextField(blank=True)

    def __str__(self):
        return str(self.solicitante)
