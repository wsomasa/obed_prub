from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App_blog import views

 
urlpatterns = [

    path('', views.blog, name='blog'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    