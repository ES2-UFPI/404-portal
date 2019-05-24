from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
  nome = forms.CharField(max_length=30, required=True)
  matricula = forms.CharField(max_length=15, required=True)
  email = forms.EmailField(max_length=100)

  class Meta:
    model = User
    fields = ('username', 'nome', 'matricula', 'email', 'password1', 'password2', )
