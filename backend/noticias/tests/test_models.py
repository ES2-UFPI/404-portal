from django.test import TestCase

from backend.noticias.models import Noticia

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Noticia.objects.create(titulo='Fim do período', subtitulo='As aulas estão acabando.', conteudo='Com o fim de periodo os alunos ficam loucos')

    def test_titulo_label(self):
        noticia = Noticia.objects.get(id=1)
        field_label = noticia._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label, 'titulo')

    def test_subtitulo_label(self):
        noticia=Noticia.objects.get(id=1)
        field_label = noticia._meta.get_field('subtitulo').verbose_name
        self.assertEquals(field_label, 'subtitulo')

    def test_titulo_max_length(self):
        noticia = Noticia.objects.get(id=1)
        max_length = noticia._meta.get_field('titulo').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_titulo(self):
        noticia = Noticia.objects.get(id=1)
        expected_object_name = noticia.titulo
        self.assertEquals(expected_object_name, str(noticia))
