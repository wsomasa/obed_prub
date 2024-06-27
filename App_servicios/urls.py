from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from App_servicios import views


 
urlpatterns = [

    path('', views.service, name='service'),
     
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    