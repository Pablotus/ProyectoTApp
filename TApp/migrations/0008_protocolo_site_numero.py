# Generated by Django 4.1.7 on 2023-04-13 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TApp', '0007_protocolo_invest_noenmasc_protocolo_invest_enmasc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocolo',
            name='site_numero',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]