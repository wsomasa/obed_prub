# Generated by Django 5.0.3 on 2024-05-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_blog', '0003_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/blog'),
        ),
    ]
