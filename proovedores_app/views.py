from django.shortcuts import render,redirect
from .models import Proveedores

# Create your views here.

# Vista para mostrar todos los proveedores
def inicio_vistaProveedor(request):
    losProveedores = Proveedores.objects.all()
    return render(request, "gestionarproveedor.html", {"losProveedores": losProveedores})

# Vista para registrar un nuevo proveedor
def registrarProveedores(request):
    idProveedor = request.POST["txtidProveedor"]
    nombre = request.POST["txtnombre"]
    fecha_nac = request.POST["txtfecha_nac"]
    sexo = request.POST["txtsexo"]
    curp = request.POST["txtcurp"]
    email = request.POST["txtemail"]
    no_telefono = request.POST["txtno_telefono"]

    GuardarProveedores=Proveedores.objects.create(
        idProveedor=idProveedor,
        nombre=nombre,
        fecha_nac=fecha_nac,
        sexo=sexo,
        curp=curp,
        email=email,
        no_telefono=no_telefono
    )

    return redirect("Proveedor")

# Vista para seleccionar un proveedor y editarlo
def seleccionarProveedores(request, idProveedor):
    proveedor = Proveedores.objects.get(idProveedor=idProveedor)
    return render(request, "editarproveedor.html", {"proveedor": proveedor})

# Vista para guardar los cambios de un proveedor editado
def editarProveedores(request):
    idProveedor = request.POST["txtidProveedor"]
    nombre = request.POST["txtnombre"]
    fecha_nac = request.POST["txtfecha_nac"]
    sexo = request.POST["txtsexo"]
    curp = request.POST["txtcurp"]
    email = request.POST["txtemail"]
    no_telefono = request.POST["txtno_telefono"]
    proveedor = Proveedores.objects.get(idProveedor=idProveedor)
    proveedor.nombre = nombre
    proveedor.fecha_nac = fecha_nac
    proveedor.sexo = sexo
    proveedor.curp = curp
    proveedor.email = email
    proveedor.no_telefono = no_telefono
    proveedor.save()  # Guarda los cambios
    return redirect("Proveedor")

# Vista para borrar un proveedor
def borrarProveedores(request, idProveedor):
    proveedor = Proveedores.objects.get(idProveedor=idProveedor)
    proveedor.delete()  # Borra el registro
    return redirect("Proveedor")
