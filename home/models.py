from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    precio = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.precio)

class Pqrs(models.Model):
    codigo = models.AutoField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    tipoPqrs = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=50)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.tipoPqrs)

class Venta(models.Model):
    codigo = models.AutoField(primary_key=True)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
    
        self.total_venta = self.producto.precio
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta #{self.codigo} - Total: {self.total_venta}"


