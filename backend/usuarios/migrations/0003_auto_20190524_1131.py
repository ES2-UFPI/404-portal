# Generated by Django 2.2 on 2019-05-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20190524_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='imagem_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='frontend/img/perfil'),
        ),
    ]
