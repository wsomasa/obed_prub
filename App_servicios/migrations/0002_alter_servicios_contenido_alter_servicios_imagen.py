
# Generated by Django 5.0.3 on 2024-05-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='contenido',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='servicios'),
        ),
    ]

