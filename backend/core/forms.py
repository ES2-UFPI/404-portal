from django import forms
from .models import Portal


class PortalForm(forms.ModelForm):
  required_css_class = 'required'

  class Meta:
    model = Portal
    fields = (
      "universidade",
      "departamento",
      "area_conhecimento",
      "nome_do_curso",
      "nome_do_coordenador",
      "nome_do_chefe_departamento",
      "rua",
      "bairro",
      "numero",
      "cep",
      "cidade",
      "estado",
      "telefone_1",
      "telefone_2",
    )
