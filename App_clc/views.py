from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login 
from .forms import CustomAuthenticationForm, RegistroForm, ContactoForm
from django.core.mail import send_mail
from django.conf import settings 
from entradas_home.models import Mision, Vision, Entradas


# vistas paginas principales
def home_view(request):
    misiones = Mision.objects.all()
    visiones = Vision.objects.all()
    entradas = Entradas.objects.all()
     
    return render(request, 'entrada/home_entrada.html', {
        'misiones': misiones,
        'visiones': visiones,
        'entradas': entradas
    })

def directorio(request):
    return render(request, 'directorio.html')

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                 
                return redirect('inicio')  
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def inicio_admin(request):
 
    return render(request, 'inicio.html')


def contact_view(request):
    if request.method =='POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje = form.cleaned_data['mensaje']
            asunto = 'Nuevo mensaje de contacto web'
            mensaje_email = f'Nombre: {nombre}\nEmail: {email}\nTeléfono: {telefono}\nMensaje: {mensaje}'
            remitente = settings.EMAIL_HOST_USER
            destinatarios = ['walterjesus.somasaamaya.ext@zeleris.com', 'wsomas@gmail.com']  
            send_mail(asunto, mensaje_email, remitente, destinatarios)
            
            return render(request, 'formulario_exitoso.html')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})    

def formulario_exitoso():
    return render('formulario_exitoso')    

def politica_privacidad(request):

    return render(request, 'politica_privacidad.html')

def aviso_legal(request):

    return render(request, 'aviso_legal.html')

def cookies(request):

    return render(request, 'cookies.html')



