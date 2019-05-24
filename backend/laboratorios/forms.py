from django.forms import ModelForm
from .models import Laboratorio


class LaboratorioForm(ModelForm):
    class Meta:
        model = Laboratorio
        fields = '__all__'