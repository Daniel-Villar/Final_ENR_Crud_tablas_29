from django.db import models

# Create your models here.
class Proveedores(models.Model):
    idProveedor = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    fecha_nac = models.DateField()  # Fecha de nacimiento
    sexo = models.CharField(max_length=10)  # Campo de sexo
    curp = models.CharField(max_length=50)
    email = models.EmailField()
    no_telefono = models.IntegerField()

    def __str__(self):
        return self.nombre
