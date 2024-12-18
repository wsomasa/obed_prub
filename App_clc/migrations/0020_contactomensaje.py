# Generated by Django 5.0.2 on 2024-05-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_clc', '0019_paciente_email_alter_documento_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactoMensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('mensaje', models.TextField()),
                ('fecha_mensaje', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
