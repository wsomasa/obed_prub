# Generated by Django 5.0.3 on 2024-05-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_clc', '0021_contacto_delete_contactomensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='archivo',
            field=models.FileField(null=True, upload_to='media_appclc'),
        ),
    ]
