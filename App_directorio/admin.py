from django.contrib import admin
from .models import Directorio



class DirectorioAdmin(admin.ModelAdmin):
    list_display= ('especialidad', 'medico', 'horario')

admin.site.register(Directorio, DirectorioAdmin)