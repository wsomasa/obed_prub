from django.contrib import admin
from .models import Categoria, Post

class CategoriaAdmin(admin.ModelAdmin):
    list_display= ('nombre',)
    readonly_fields= ('created', 'update')

class PostAdmin(admin.ModelAdmin):
    list_display= ('titulo', 'contenido', 'autor', 'imagen')
    readonly_fields= ('created', 'update')

admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Post, PostAdmin)

