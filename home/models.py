from django.db import models

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    precio = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.precio})"

class Pqrs(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    tipoPqrs = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=1000)
    
    def __str__(self):
        return f"{self.nombre} ({self.tipoPqrs})"

class Venta(models.Model):
    codigo = models.AutoField(primary_key=True)
    total_venta = models.DecimalField(max_digits=10, decimal_places=0)
    productos = models.ManyToManyField(Producto, through='VentaProducto')

    def __str__(self):
        return f"Venta #{self.codigo} - Total: {self.total_venta}"

class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"Venta #{self.venta.codigo}: {self.cantidad} de {self.producto.nombre}"
