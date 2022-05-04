from django.db import models


# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField(max_length=100)
    ciudad=models.CharField(max_length=50)
    telefono=models.CharField(max_length=15)

    def _str_(self):
        return self.apellido

class Pedido(models.Model):
    nombre=models.CharField(max_length=50)
    contacto= models.CharField(max_length=50)
    pedido=models.CharField(max_length=50)

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.CharField(max_length=50)
    detalle=models.CharField(max_length=50)
    cantidad=models.CharField(max_length=50)
    proveedor=models.CharField(max_length=50)

class Proveedor(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.CharField(max_length=50)
    correo=models.EmailField(max_length=100)
    ciudad=models.CharField(max_length=50)
    telefono=models.CharField(max_length=15)

