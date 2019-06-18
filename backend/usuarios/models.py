from django.db import models
from django.contrib.auth.models import User


VINCULOS_PESSOA = [
    ("Aluno", "Aluno"),
    ("Coordenador", "Coordenador")
]

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    registro = models.CharField(max_length=15)
    email = models.EmailField()
    aprovado = models.BooleanField(default=False, blank=False)
    tipo = models.CharField(max_length=20, choices=VINCULOS_PESSOA)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome