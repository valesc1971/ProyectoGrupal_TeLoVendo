from django.contrib import admin
from .models import Cliente, Comentario, Pedido, Producto, Proveedor

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Comentario)