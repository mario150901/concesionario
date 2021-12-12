from django.contrib import admin

from catalogo.models import Coche, Fabricante

# Register your models here.
@admin.register(Coche)
class CocheAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo']
    list_filter = ['nombre_fabricante']

@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ['nombre_fabricante']
