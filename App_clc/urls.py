from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from App_clc import views

urlpatterns = [
    path('inicio_admin/', views.inicio_admin, name='inicio_admin'), 
    path('index/', views.index, name= 'index'),
    path('directorio/', views.directorio, name='directorio'),
    path('contacto/', views.contact_view, name='contacto'),
    path('politica_privacidad/', views.politica_privacidad, name='politica_privacidad'),
    path('aviso_legal/', views.aviso_legal, name='aviso_legal'),
    path('cookies/', views.cookies, name='cookies'),   
   
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
