# Generated by Django 5.0.3 on 2024-05-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media_blog')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
            },
        ),
    ]