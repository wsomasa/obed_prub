from django.db import models
from django.contrib.auth.models import User
     
class Mision(models.Model):
    #imagen=models.ImageField(upload_to='media/mision', null=True, blank=True)
    titulo = models.CharField(max_length=50, null=True, blank=True)
    contenido=models.TextField()

    class Meta:
        verbose_name='mision'
        verbose_name_plural='misiones'
    
    def __str__(self):
        
        return f"{self.titulo} - {self.contenido}"
    
class Vision(models.Model):
    #imagen=models.ImageField(upload_to='media/visiones', null=True, blank=True)
    titulo = models.CharField(max_length=50, null=True, blank=True)
    contenido=models.TextField()

    class Meta:
        verbose_name='vision'
        verbose_name_plural='visiones'
    
    def __str__(self):
        
        return f"{self.titulo} - {self.contenido}"

class Entradas(models.Model):
    imagen=models.ImageField(upload_to='media/entradas', null=True, blank=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    contenido=models.TextField()

    class Meta:
        verbose_name='entrada'
        verbose_name_plural='entradas'
    
    def __str__(self):
        
        return f"{self.titulo} - {self.contenido}"
    
    
    
