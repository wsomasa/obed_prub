# Generated by Django 5.0.3 on 2024-06-22 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entradas_home', '0002_mision_vision_delete_entrada_home'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mision',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='vision',
            name='imagen',
        ),
    ]
