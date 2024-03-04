from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    precio = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.precio)

class Pqrs(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    tipoPqrs = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=50)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.tipoPqrs)

class Venta(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    productos = models.ManyToManyField(Producto) 
    totalVenta = models.CharField(max_length=51)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nomProducto, self.totalVenta)

