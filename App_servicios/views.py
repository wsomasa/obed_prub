from django.shortcuts import render
from .models import Servicios

def service(request):
    
    servicios=Servicios.objects.all() #aquí importamos todos los post creados
    return render(request, 'servicios/service.html', {'servicios': servicios})