# Generated by Django 5.0.3 on 2024-04-15 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_clc', '0011_paciente_cedula_pasaporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1),
        ),
    ]