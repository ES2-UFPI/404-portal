from django.test import TestCase
from backend.salas.models import Sala
from backend.usuarios.models import Pessoa
from backend.salas.forms import SalaForm


class HierarquiaTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Pessoa.objects.create(
            nome="pessoinha",
            registro="123447854",
            email = "p@mail.com",
            aprovado = True,
            tipo = "Aluno"
        )

        Pessoa.objects.create(
            nome="pessoinha C",
            registro="1234478547848",
            email = "pc@mail.com",
            aprovado = True,
            tipo = "Coordenador"
        )
        

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/salas/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['salas']), 0)
        
    def test_cadastro_de_sala(self):
        form_data = {
            'numero':87,
            'capacidade':8,
            'latitude':1,
            'longitude':1
        }
        
        form = SalaForm(data = form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post('/salas/cadastrar', form_data)
        self.assertEqual(response.status_code,302)
        response = self.client.get('/salas/')
        self.assertEqual(len(response.context['salas']), 0)