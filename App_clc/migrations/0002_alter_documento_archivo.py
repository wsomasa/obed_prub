# Generated by Django 5.0.3 on 2024-03-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_clc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='archivo',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]
