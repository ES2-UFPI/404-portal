# Generated by Django 2.2.1 on 2019-05-20 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='sala',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]