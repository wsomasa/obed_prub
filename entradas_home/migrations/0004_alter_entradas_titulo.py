# Generated by Django 5.0.3 on 2024-06-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entradas_home', '0003_remove_mision_imagen_remove_vision_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas',
            name='titulo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
