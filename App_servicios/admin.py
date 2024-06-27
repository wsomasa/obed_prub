from django.contrib import admin
from .models import Servicios



class ServicioAdmin(admin.ModelAdmin):
    list_display= ('especialidad', 'contenido', 'imagen')

admin.site.register(Servicios, ServicioAdmin)

