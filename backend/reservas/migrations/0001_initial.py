from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('laboratorios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('justificativa', models.TextField()),
                ('data_hora_reserva', models.DateTimeField(null=True)),
                ('data_hora_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('avaliada', models.BooleanField(default=False)),
                ('aceita', models.BooleanField(default=False)),
                ('comentario', models.TextField(blank=True)),
                ('avaliada_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('laboratorio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='laboratorios.Laboratorio')),
                ('sala', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='salas.Sala')),
                ('solicitante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
