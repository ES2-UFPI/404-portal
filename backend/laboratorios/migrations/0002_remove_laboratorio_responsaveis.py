# Generated by Django 2.2 on 2019-04-29 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratorio',
            name='responsaveis',
        ),
    ]
