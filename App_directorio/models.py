
from django.db import models
from django.contrib.auth.models import User

class Directorio(models.Model):
    especialidad = models.CharField(max_length=50)
    medico=models.CharField(max_length=50)
    horario = models.CharField(max_length=50)  
    
    class Meta:
        verbose_name='especialidad'
        verbose_name_plural='especialidades'
        
    def __str__(self):
        
        return f"{self.especialidad} - {self.medico} - {self. horario}"