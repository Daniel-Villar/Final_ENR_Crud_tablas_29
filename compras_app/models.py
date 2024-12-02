from django.db import models

# Create your models here.

class Compras(models.Model):
    idCompra = models.CharField(primary_key=True, max_length=6)
    idprovedor = models.CharField(max_length=6)
    idEmpleado = models.CharField(max_length=6)
    idProducto = models.CharField(max_length=6)
    cantidad = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateField()

    def __str__(self):
        return f'Compra {self.idCompra}'
