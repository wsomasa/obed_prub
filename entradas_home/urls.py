from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from entradas_home import views

 
urlpatterns = [

    path('', views.home_view, name='entrada_home'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    