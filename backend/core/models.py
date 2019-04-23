from django.db import models

class admin (model.Model):
	nome = model.CharField(max length = 100)
	email = model.EmailField(max length = 100)
	cpf = model.CharField(max length = 12)
	celular = model.CharField(max length = 10)
	telefone2 = model.CharField(max length = 10)

class curso (model.Model):
	nome = model.CharField(max length = 100)
	universidade = model.CharField(max length = 100)
	nome_chefe_departamento = model.CharField(max length = 100)
	nome_coordenador = model.CharField(max length = 100)
	departamento = model.CharField(max length = 100)
	area_de_conhecimento = model.CharField(max length = 100)
	cidade = model.CharField(max length = 100)
	estado = model.CharField(max length = 100)
	cep = model.CharField(max length = 20)
	rua = model.CharField(max length = 100)
	bairro = model.CharField(max length = 100)
	numero = model.CharField(max length = 10)
	email = model.EmailField(max length = 100)
	telefone1 = model.CharField(max length = 10)
	telefone2 = model.CharField(max length = 10)
