# Generated by Django 5.0.3 on 2024-04-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_clc', '0014_cirugia_enfermeros_cirugia_medicos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cirugia',
            name='enfermeros',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cirugia',
            name='medicos',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cirugia',
            name='tipo',
            field=models.CharField(choices=[('A', 'Artroscopia'), ('R', 'Reemplazo articular'), ('L', 'Cirugía de ligamentos'), ('C', 'Cirugía de columna'), ('CR', 'Cirugía reconstructiva'), ('CMM', 'Cirugía de mano y muñeca')], default='seleccionar', max_length=3),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='motivo',
            field=models.CharField(choices=[('V', 'Valoración'), ('PRO', 'Pre Operatorio'), ('PO', 'Post Operatorio'), ('PC', 'Primera cita'), ('SC', 'Segunda cita')], default='seleccionar', max_length=3),
        ),
    ]
