# Generated by Django 4.2 on 2023-04-09 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TApp', '0002_protocolo_rename_site_paciente_site_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numero_paciente',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
