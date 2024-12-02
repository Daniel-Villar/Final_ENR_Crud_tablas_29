from django.db import models

class Productos(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=1)
    nombre = models.CharField(max_length=100)
    Precio =  models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio_mayoreo = models.CharField(max_length=100)
    stock =  models.CharField(max_length=100)
    demanda =  models.CharField(max_length=100)
    idSucursal = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre
