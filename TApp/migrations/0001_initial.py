# Generated by Django 4.2 on 2023-04-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.IntegerField(unique=True)),
                ('telefono', models.IntegerField(unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('protocolo', models.CharField(max_length=40)),
                ('numero_paciente', models.IntegerField(unique=True)),
                ('ojo_estudio', models.CharField(max_length=2)),
                ('site', models.CharField(max_length=40)),
                ('fecha_rando', models.DateField()),
            ],
        ),
    ]
