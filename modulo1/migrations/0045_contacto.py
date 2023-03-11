# Generated by Django 4.1.3 on 2023-03-11 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo1', '0044_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'sugerencias'], [3, 'felicitaciones']])),
                ('mensaje', models.TextField()),
                ('aviso', models.BooleanField()),
            ],
        ),
    ]
