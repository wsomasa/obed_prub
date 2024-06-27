# scripts/enviar_recordatorio_consulta.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date, timedelta
from django.core.mail import send_mail
from App_clc.models import Consulta

def enviar_recordatorio_consulta():
    # Obtener todas las consultas próximas en los próximos 3 días
    consultas_proximas = Consulta.objects.filter(proxima_consulta__lte=date.today() + timedelta(days=3))

    for consulta in consultas_proximas:
        # Configurar el correo electrónico
        mensaje = MIMEMultipart()
        mensaje['From'] = 'wsomas@gmail.com'
        mensaje['To'] = consulta.paciente.correo
        mensaje['Subject'] = 'Recordatorio de próxima consulta'

        # Cuerpo del correo electrónico
        cuerpo_mensaje = f'Hola {consulta.paciente.nombre},\n\nEste es un recordatorio amistoso de que tienes una consulta médica el {consulta.proxima_consulta}. Por favor, asegúrate de asistir a tiempo.\n\nAtentamente,\nTu Clínica Médica'

        mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

        # Enviar el correo electrónico
        servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_smtp.starttls()
        servidor_smtp.login('wsomas@gmail.com', 'merida10.M')
        texto = mensaje.as_string()
        servidor_smtp.sendmail('wsomas@gmail.com', consulta.paciente.correo, texto)
        servidor_smtp.quit()

if __name__ == '__main__':
    enviar_recordatorio_consulta()
