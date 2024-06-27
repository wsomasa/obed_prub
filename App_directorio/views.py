from django.shortcuts import render
from .models import Directorio

def directorio(request):
    
    directorios=Directorio.objects.all() #aquí importamos todos los post creados
    return render(request, 'directorio/directorio.html', {'directorios': directorios})
