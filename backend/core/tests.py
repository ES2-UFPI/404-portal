from django.test import TestCase
from django.urls import reverse
from ..core.models import Portal

USERNAME = "username_test"
PASSWORD = "password_test"


class PortalTestCase(TestCase):

  @classmethod
  def setUpTestData(self):
    portal = Portal.objects.create()
    portal.email = "teste@teste.com"
    portal.nome_solicitante = "Username Teste"
    portal.cpf_solicitante = "000.000.000-00"
    portal.email_solicitante = "solicitante@teste.com"
    portal.telefone_solicitante = "(86) 3200-0000"
    portal.celular_solicitante = "(86) 9500-0000"
    portal.universidade = "Universidade Federal do Piauí"
    portal.departamento = "Computação"
    portal.area_conhecimento = "Ciências da Natureza, Exatas"
    portal.nome_do_curso = "Ciência da Computação"
    portal.nome_do_coordenador = "Coordenador Teste"
    portal.nome_do_chefe_departamento = "Chefe Teste"
    portal.cidade = "Teresina"
    portal.estado = "Piauí"
    portal.cep = "64012-000"
    portal.bairro = "Ininga"
    portal.rua = "Petrônio Portela"
    portal.numero = "0000"
    portal.telefone_1 = "(86) 3201-0000"
    portal.telefone_2 = "(86) 3202-0000"
    portal.save()


class CoreTestCase(PortalTestCase):
  def test_home(self):
    self.client.login(username=USERNAME, password=PASSWORD)
    resp = self.client.get(reverse('core:home'))
    self.assertEqual(resp.status_code, 200)

  def test_listar(self):
    self.client.login(username=USERNAME, password=PASSWORD)
    resp = self.client.get(reverse('core:listar'))
    self.assertEqual(resp.status_code, 200)

  def test_visualizar(self):
    portal = Portal.objects.get(nome_do_curso="Ciência da Computação")
    self.client.login(username=USERNAME, password=PASSWORD)
    resp = self.client.get(reverse('core:visualizar', kwargs={'id': portal.id}))
    self.assertEqual(resp.status_code, 200)

  def test_editar(self):
    portal = Portal.objects.get(nome_do_curso="Ciência da Computação")
    self.client.login(username=USERNAME, password=PASSWORD)
    self.assertEqual(portal.email, "teste@teste.com")
    self.assertEqual(portal.nome_solicitante, "Username Teste")
    self.assertEqual(portal.cpf_solicitante, "000.000.000-00")
    self.assertEqual(portal.email_solicitante, "solicitante@teste.com")
    self.assertEqual(portal.telefone_solicitante, "(86) 3200-0000")
    self.assertEqual(portal.celular_solicitante, "(86) 9500-0000")
    self.assertEqual(portal.universidade, "Universidade Federal do Piauí")
    self.assertEqual(portal.departamento, "Computação")
    self.assertEqual(portal.area_conhecimento, "Ciências da Natureza, Exatas")
    self.assertEqual(portal.nome_do_coordenador, "Coordenador Teste")
    self.assertEqual(portal.nome_do_curso, "Ciência da Computação")
    self.assertEqual(portal.nome_do_chefe_departamento, "Chefe Teste")
    self.assertEqual(portal.cidade, "Teresina")
    self.assertEqual(portal.estado, "Piauí")
    self.assertEqual(portal.cep, "64012-000")
    self.assertEqual(portal.bairro, "Ininga")
    self.assertEqual(portal.rua, "Petrônio Portela")
    self.assertEqual(portal.numero, "0000")
    self.assertEqual(portal.telefone_1, "(86) 3201-0000")
    self.assertEqual(portal.telefone_2, "(86) 3202-0000")
    url = reverse('core:editar', kwargs={'id': portal.id})
    resp = self.client.get(url)
    self.assertEqual(resp.status_code, 200)
    POST = {
      "area_conhecimento": "Exatas"
    }
    resp = self.client.post(url, POST)
    self.assertEqual(302, resp.status_code)
    portal = Portal.objects.get(nome_do_curso="Ciência da Computação")
    self.assertEqual(portal.area_conhecimento, "Exatas")

  def test_login(self):
    self.client.login(username=USERNAME, password=PASSWORD)
    url = reverse('core:login')
    resp = self.client.get(url)
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(url, '/login/')

  def test_logout(self):
    self.client.login(username=USERNAME, password=PASSWORD)
    url = reverse('core:logout')
    resp = self.client.get(url)
    self.assertEqual(resp.status_code, 302)
    self.assertEqual(url, '/logout/')
    self.assertRedirects(resp, '/')
