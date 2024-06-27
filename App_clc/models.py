
from django.db import models
from django.contrib.auth.models import User
from django.db import models




class Paciente(models.Model):
    cedula_identidad = models.CharField(max_length=20, default='default_value')  
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email=models.EmailField(blank=True, null=True)
    edad = models.IntegerField()
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default= 'M')
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    def __str__(self):
 
        return "{} - {}".format(self.nombre, self.cedula_identidad)
    
    class lista_paciente(models.Model):
        pass

 
class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    MOTIVO_CONSULTA = [
        ('V', 'Valoración'),
        ('PRO', 'Pre operatorio'),
        ('PO', 'Post operatorio'),
        ('PC', 'Primera cita'),
        ('SC', 'Segunda cita'),
        ('TC', 'Tercera cita'),
        ('CC', 'Cuarta cita'),
        ('QC', 'Quinta cita'),
        ('CO', 'Cita opcional'),
    ]
    motivo = models.CharField(max_length=3, choices=MOTIVO_CONSULTA, default= 'seleccionar')      
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    archivos = models.FileField('Archivo', blank=True)
    proxima_consulta = models.DateField(null=True, blank=True)
 
    def __str__(self):
        return f"Consulta de {self.paciente.nombre} - {self.fecha}"

class Archivo(models.Model):
    consulta_relacionada = models.ForeignKey(Consulta, on_delete=models.CASCADE, related_name='archivos_relacionados')
    archivo = models.FileField(upload_to='archivos_consulta/')
 
class Cirugia(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    TIPO_CIRUGIA = [
        ('A', 'Artroscopia'),
        ('R', 'Reemplazo articular'),
        ('L', 'Cirugía de ligamentos'),
        ('C', 'Cirugía de columna'),
        ('CR', 'Cirugía reconstructiva'),
        ('CMM', 'Cirugía de mano y muñeca'),
    ]
    tipo = models.CharField(max_length=3, choices=TIPO_CIRUGIA, default= 'seleccionar')
    resultado = models.TextField()
    medicos = models.TextField()
    enfermeros = models.TextField()
    personal_externo = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Cirugía de {self.paciente.nombre} - {self.fecha}"
    
class Documento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    TIPO_DOCUMENTO = [
        ('ICH', 'Informe clínico hospitalización'),
        ('ICCE', 'Informe clínico consulta externa'),
        ('ICE', 'Informe clínico de emergencias'),
        ('IMAP', 'Informe médico de atención primaria'),
        ('IRPL', 'Informe de resultados de pruebas de laboratorio'),
        ('ICH', 'Informe de resultados de pruebas de imagen'),
        ('ICE', 'Informe de cuidados de enfermeria'),
    ]
    tipo = models.CharField(max_length=4, choices=TIPO_DOCUMENTO, default= 'seleccionar')
    archivo = models.FileField(upload_to='clinica', null=True) #aquí le indicamos en cual carpeta va almacenar la imagen o el archivo
    descripcion = models.TextField()
    
    def __str__(self):
        return f"Documento de {self.archivo} - {self.descripcion}"
    


#formulario de contacto



class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length= 15)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
