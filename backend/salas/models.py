from django.db import models
from django.contrib.auth.models import User


class Sala(models.Model):
  numero = models.PositiveIntegerField()
  capacidade = models.PositiveIntegerField()
  reservada = models.BooleanField(default=False)
  reservada_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):
    return str(self.numero)
