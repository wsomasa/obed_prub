# Generated by Django 5.0.3 on 2024-04-06 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_clc', '0008_historiageneral'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='usuario',
        ),
    ]
