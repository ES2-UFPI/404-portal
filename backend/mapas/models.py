from django.db import models


class Mapa(models.Model):
    nome = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nome