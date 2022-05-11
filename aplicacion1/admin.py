from django.contrib import admin
from django.urls import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe
from .models import Cliente, Comentario, Pedido, Producto, Proveedor, Categoria, Subcategoria


# Register your models here.

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Comentario)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Subcategoria)

"""
class ProveedorAdmin(admin.ModelAdmin):

    list_display = ["categoria", "subcategoria", "related"]
    list_display_links = ["categoria", "related"]

"""
