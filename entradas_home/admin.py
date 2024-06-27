from django.contrib import admin
from .models import Mision, Vision, Entradas


class MisionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido')
admin.site.register(Mision, MisionAdmin)    


class VisionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido')
admin.site.register(Vision, MisionAdmin) 

class EntradasAdmin(admin.ModelAdmin):
    list_display= ('titulo', 'contenido', 'imagen')
    
admin.site.register(Entradas, EntradasAdmin)

