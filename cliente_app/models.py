from django.db import models

class Clientes(models.Model):
    idCliente = models.CharField(primary_key=True, max_length=1)
    nombre = models.CharField(max_length=100)
    Fecha_nac = models.DateField()  # Cambiado a DateField
    sexo = models.CharField(max_length=100)
    no_telefono = models.IntegerField()
    Direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
