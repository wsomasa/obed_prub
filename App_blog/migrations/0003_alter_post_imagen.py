
# Generated by Django 5.0.3 on 2024-05-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_blog', '0002_alter_post_options_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
    ]