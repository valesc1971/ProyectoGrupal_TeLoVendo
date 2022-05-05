from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.productos, name='productos'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('clientes/', views.clientes, name='clientes'),
    path('ingreso_clientes/', views.ingreso_clientes, name='ingreso_clientes'),
    path('login/', views.login, name='login'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('salir/', views.salir, name='salir'),
    path('register/', views.register, name='register'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('comentario_clientes/', views.comentario_clientes, name='comentario_clientes'),
    path('lista_comentarios/', views.lista_comentarios, name='lista_comentarios'),
]
