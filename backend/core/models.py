from django.db import models
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords


class BaseModel(TimeStampedModel):
  class Meta:
    abstract = True
  history = HistoricalRecords(inherit=True)
  changed_by = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)
  deleted = models.BooleanField(default=False)

  @property
  def _history_user(self):
    return self.changed_by

  @_history_user.setter
  def _history_user(self, value):
    self.changed_by = value

class Portal(BaseModel):
  email = models.CharField("E-mail", max_length=100, blank=True, default="")
  nome_solicitante = models.CharField("Nome do Solicitante", max_length=255, blank=True, default="")
  cpf_solicitante = models.CharField("CPF do Solicitante", max_length=30, blank=True, default="")
  email_solicitante = models.CharField("E-mail do Solicitante", max_length=100, blank=True, default="")
  telefone_solicitante = models.CharField("Telefone do Solicitante", max_length=30, blank=True, default="")
  celular_solicitante = models.CharField("Celular do Solicitante", max_length=30, blank=True, default="")
  universidade = models.CharField("Universidade", max_length=255, blank=True, default="")
  departamento = models.CharField("Departamento", max_length=255, blank=True, default="")
  area_conhecimento = models.CharField("Área de Conhecimento", max_length=100, blank=True, default="")
  nome_do_curso = models.CharField("Nome do Curso", max_length=255, blank=True, default="")
  nome_do_coordenador = models.CharField("Nome do Coordenador", max_length=255, blank=True, default="")
  nome_do_chefe_departamento = models.CharField("Nome do Chefe de Departamento", max_length=255, blank=True, default="")
  cidade = models.CharField("Cidade", max_length=50, blank=True, default="")
  estado = models.CharField("Estado", max_length=30, blank=True, default="")
  cep = models.CharField("CEP", max_length=30, blank=True, default="")
  bairro = models.CharField("Bairro", max_length=255, blank=True, default="")
  rua = models.CharField("Rua", max_length=100, blank=True, default="")
  numero = models.CharField("Número", max_length=10, blank=True, default="")
  telefone_1 = models.CharField("Telefone 1", max_length=30, blank=True, default="")
  telefone_2 = models.CharField("Telefone 2", max_length=30, blank=True, default="")

  def __str__(self):
    return self.nome_do_curso

  def create(self, **kwargs):
    query = Portal.objects.all()
    if query.exists():
      raise Exception("Portal já existe!")
    else:
      return super().create(**kwargs)

  def save(self, **kwargs):
    query = Portal.objects.all()
    if self.id == None and query.exists():
      raise Exception("Portal já existe!")
    else:
      return super().save(**kwargs)

  def delete(self):
    self.deleted = True
    self.save()
