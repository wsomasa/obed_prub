from django.db import models
from django.contrib.auth.models import User

class Servicios(models.Model):
    especialidad = models.CharField(max_length=50)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to='media/servicios', null=True, blank=True)  
    
    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
        
    def __str__(self):
        
        return f"{self.especialidad} - {self.contenido}"