from django.forms import ModelForm
from .models import Evento


class EventoForm(ModelForm):
    class Meta:
        model = Evento
        exclude = ('data_publicacao',)