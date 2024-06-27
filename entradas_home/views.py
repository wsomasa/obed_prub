from django.shortcuts import render, get_object_or_404
from entradas_home.models import Mision, Vision, Entradas


    
def home_view(request):
    misiones = Mision.objects.all()
    visiones = Vision.objects.all()
    entradas = Entradas.objects.all()
     
    return render(request, 'entrada/home_entrada.html', {
        'misiones': misiones,
        'visiones': visiones,
        'entradas': entradas
    })

    #politica privacidad

def politica(request):
    return render(request, 'politica_privacidad.html')