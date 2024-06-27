from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre= models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        
    def __str__(self):
        
        return self.nombre 
        
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido=models.TextField()

    imagen=models.ImageField(upload_to='media/blog', null=True, blank=True)  #indicamos que la imagene es opcional con los ultimos argumentos
    autor=models.ForeignKey(User, on_delete=models.CASCADE) #indicamos que cuando se elimine el autor, elimine todos los pots que ese autor haya creado.
    cateqorias=models.ManyToManyField(Categoria) #aqui indicamos que relaciones las categorias.
    
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    
    
    
