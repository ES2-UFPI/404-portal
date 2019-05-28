from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Pessoa

class PessoaForm(ModelForm):
  class Meta:
    model = Pessoa
    exclude = ['user', 'aprovado']