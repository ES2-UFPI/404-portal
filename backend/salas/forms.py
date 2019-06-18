from django.forms import ModelForm
from .models import Sala


class SalaForm(ModelForm):

	class Meta:
	    model = Sala
	    fields = ('numero', 'capacidade', 'reservada', 'reservada_por','latitude','longitude')


