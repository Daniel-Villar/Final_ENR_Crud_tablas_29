from django.db import models

class Sucursales(models.Model):
    idSucursales = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    num_telefono = models.CharField(max_length=15) 
    horario = models.CharField(max_length=50)
    empleados=models.CharField(max_length=100)
    email = models.EmailField() 
    

    def __str__(self):
        return self.nombre
