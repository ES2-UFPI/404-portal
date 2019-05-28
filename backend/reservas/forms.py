from django.forms import ModelForm
from .models import Reserva


class ReservaForm(ModelForm):
  class Meta:
    model = Reserva
    exclude = ('data_hora_criacao', 'solicitante', 'avaliada_por', 'avaliada', 'aceita', 'comentario')

class AvaliarReservaForm(ModelForm):
  class Meta:
    model = Reserva
    fields = ('comentario', 'aceita')
