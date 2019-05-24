from django.db import models
from django.utils import timezone


class Noticia(models.Model):
  titulo = models.CharField(max_length = 50)
  subtitulo = models.TextField()
  conteudo = models.TextField()
  data_criacao = models.DateTimeField(default = timezone.now)
  data_publicacao = models.DateTimeField(null = True, blank = True)

  def __str__(self):
    return self.titulo
