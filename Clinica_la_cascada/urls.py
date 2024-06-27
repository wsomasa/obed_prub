from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from App_clc import views
from entradas_home import views




urlpatterns = [
    
    path('', views.home_view, name='entrada_home'),
    path('admin/', admin.site.urls), 
    path('home/', include('App_clc.urls')),
    path('directorio/', include('App_directorio.urls')),
    path('blog/', include('App_blog.urls')),
    path('servicios/', include('App_servicios.urls')), 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
