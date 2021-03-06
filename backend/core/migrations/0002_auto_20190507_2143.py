# Generated by Django 2.2 on 2019-05-08 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portal',
            name='endereco',
        ),
        migrations.AddField(
            model_name='portal',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='portal',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='portal',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='portal',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='area_conhecimento',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Área de Conhecimento'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='bairro',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='celular_solicitante',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Celular do Solicitante'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='cep',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='cidade',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='cpf_solicitante',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='CPF do Solicitante'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='departamento',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='email_solicitante',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='E-mail do Solicitante'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='estado',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='nome_do_chefe_departamento',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Nome do Chefe de Departamento'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='nome_do_coordenador',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Nome do Coordenador'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='nome_do_curso',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Nome do Curso'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='nome_solicitante',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Nome do Solicitante'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='numero',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='rua',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Rua'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='telefone_1',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Telefone 1'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='telefone_2',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Telefone 2'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='telefone_solicitante',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Telefone do Solicitante'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='universidade',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Universidade'),
        ),
        migrations.CreateModel(
            name='HistoricalPortal',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('deleted', models.BooleanField(default=False)),
                ('email', models.CharField(blank=True, default='', max_length=100, verbose_name='E-mail')),
                ('nome_solicitante', models.CharField(blank=True, default='', max_length=255, verbose_name='Nome do Solicitante')),
                ('cpf_solicitante', models.CharField(blank=True, default='', max_length=30, verbose_name='CPF do Solicitante')),
                ('email_solicitante', models.CharField(blank=True, default='', max_length=100, verbose_name='E-mail do Solicitante')),
                ('telefone_solicitante', models.CharField(blank=True, default='', max_length=30, verbose_name='Telefone do Solicitante')),
                ('celular_solicitante', models.CharField(blank=True, default='', max_length=30, verbose_name='Celular do Solicitante')),
                ('universidade', models.CharField(blank=True, default='', max_length=255, verbose_name='Universidade')),
                ('departamento', models.CharField(blank=True, default='', max_length=255, verbose_name='Departamento')),
                ('area_conhecimento', models.CharField(blank=True, default='', max_length=100, verbose_name='Área de Conhecimento')),
                ('nome_do_curso', models.CharField(blank=True, default='', max_length=255, verbose_name='Nome do Curso')),
                ('nome_do_coordenador', models.CharField(blank=True, default='', max_length=255, verbose_name='Nome do Coordenador')),
                ('nome_do_chefe_departamento', models.CharField(blank=True, default='', max_length=255, verbose_name='Nome do Chefe de Departamento')),
                ('cidade', models.CharField(blank=True, default='', max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, default='', max_length=30, verbose_name='Estado')),
                ('cep', models.CharField(blank=True, default='', max_length=30, verbose_name='CEP')),
                ('bairro', models.CharField(blank=True, default='', max_length=255, verbose_name='Bairro')),
                ('rua', models.CharField(blank=True, default='', max_length=100, verbose_name='Rua')),
                ('numero', models.CharField(blank=True, default='', max_length=10, verbose_name='Número')),
                ('telefone_1', models.CharField(blank=True, default='', max_length=30, verbose_name='Telefone 1')),
                ('telefone_2', models.CharField(blank=True, default='', max_length=30, verbose_name='Telefone 2')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('changed_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical portal',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
