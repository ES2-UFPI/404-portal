from django.db import models
from django.contrib.auth.models import User


class Laboratorio(models.Model):
    nome = models.CharField(max_length=50)
    capacidade = models.PositiveIntegerField()
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    reservado = models.BooleanField(default=False)
    reservado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
