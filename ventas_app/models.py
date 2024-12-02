from django.db import models

class Ventas(models.Model):
    idVentas = models.CharField(primary_key=True, max_length=1)
    idEmpleado = models.CharField(max_length=6)
    idCliente =  models.CharField(max_length=6)
    idProductos = models.CharField(max_length=6)
    idSucursal = models.CharField(max_length=6)
    fecha_venta =  models.CharField(max_length=6)
    cantidad =  models.CharField(max_length=6)
    total = models.CharField(max_length=6)
    

    def __str__(self):
        return self.idVentas
