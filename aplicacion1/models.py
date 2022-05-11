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

class Subcategoria(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="nombre subcategoria")

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="nombre categoria")

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
    subcategoria=models.ForeignKey(Subcategoria, null=True, on_delete=models.CASCADE) 
    correo=models.EmailField(max_length=100)
    ciudad=models.CharField(max_length=50)
    telefono=models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField(max_length=100)
    comentario=models.CharField(max_length=150)


