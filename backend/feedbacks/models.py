from django.db import models
from django.utils import timezone


class Feedback(models.Model):
    assunto = models.CharField(max_length = 50)
    descricao = models.TextField()
    email = models.CharField(max_length = 100)
    data_criacao = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.assunto