from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Feedback
from .forms import FeedbackForm
from backend.usuarios.models import Pessoa

def listar(request):
  pessoa = None
  if request.user.is_authenticated:
    user = request.user
    pessoa = Pessoa.objects.get(user=user)
  feedbacks = Feedback.objects.all().order_by('-data_criacao')
  return render(request, 'feedbacks/listar.html', {'feedbacks': feedbacks, 'pessoa': pessoa})

def visualizar(request, id):
  feedback = get_object_or_404(Feedback, id = id)
  return render(request, 'feedbacks/visualizar.html', {'feedback': feedback})

@login_required
def cadastrar(request):
  if request.method == "POST":
    form = FeedbackForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('feedbacks:listar')
  else:
    form = FeedbackForm()
    return render(request, 'feedbacks/editar.html', {'form': form})

@login_required
def editar(request, id):
  feedback = get_object_or_404(Feedback, id = id)
  if request.method == "POST":
    form = FeedbackForm(request.POST, instance = feedback)
    if form.is_valid():
      form.save()
    return redirect('feedbacks:listar')
  else:
    form = FeedbackForm(instance = feedback)
    return render(request, 'feedbacks/editar.html', {'form': form})

@login_required
def remover(request, id):
  feedback = get_object_or_404(Feedback, id = id)
  feedback.delete()
  return redirect('feedbacks:listar')
