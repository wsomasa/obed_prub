# Generated by Django 5.0.3 on 2024-04-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_clc', '0017_lista_paciente_remove_registroimpresion_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='motivo',
            field=models.CharField(choices=[('V', 'Valoración'), ('PRO', 'Pre operatorio'), ('PO', 'Post operatorio'), ('PC', 'Primera cita'), ('SC', 'Segunda cita'), ('TC', 'Tercera cita'), ('CC', 'Cuarta cita'), ('QC', 'Quinta cita'), ('CO', 'Cita opcional')], default='seleccionar', max_length=3),
        ),
    ]
