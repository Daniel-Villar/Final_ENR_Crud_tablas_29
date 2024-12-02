from django.shortcuts import render, redirect
from .models import Sucursales

# Create your views here.
def inicio_vistaSucursales(request):
    lasSucursales = Sucursales.objects.all()
    return render(request, "gestionarsucursales.html", {"LasSucursales2": lasSucursales})

def registrarSucursales(request):
    idSucursales = request.POST["txtidsucursal"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    num_telefono = request.POST["txtnumtelefono"]
    horario = request.POST["txthorario"]
    empleados = request.POST["txtempleados"]
    email = request.POST["txtemail"]

    guardarSucursales = Sucursales.objects.create(
        idSucursales=idSucursales,
        nombre=nombre,
        direccion=direccion,
        num_telefono=num_telefono,
        horario=horario,
        empleados=empleados,
        email=email
    )  # Guarda el Registro

    return redirect("Sucursal")

def seleccionarSucursales(request, idSucursales):
    sucursal = Sucursales.objects.get(idSucursales=idSucursales)
    return render(request, "editarsucursales.html", {"lasSucursal": sucursal})

def editarSucursales(request):
    idSucursales = request.POST["txtidsucursal"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    num_telefono = request.POST["txttelefono"]
    horario = request.POST["txthorario"]
    empleados = request.POST["txtempleados"]
    email = request.POST["txtemail"]

    sucursal = Sucursales.objects.get(idSucursales=idSucursales)
    sucursal.nombre = nombre
    sucursal.direccion = direccion
    sucursal.num_telefono = num_telefono
    sucursal.horario = horario
    sucursal.empleados = empleados
    sucursal.email = email
    sucursal.save()  

    return redirect("Sucursal")

def borrarSucursales(request, idSucursales):
    sucursal = Sucursales.objects.get(idSucursales=idSucursales)
    sucursal.delete()  # Borra el registro
    return redirect("Sucursal")
