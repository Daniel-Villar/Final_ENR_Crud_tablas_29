from django.shortcuts import render, redirect
from .models import Compras

# Mostrar todas las compras
def inicio_vistaCompras(request):
    lasCompras = Compras.objects.all()
    return render(request, "gestionarcompras.html", {"lasCompras": lasCompras})

# Registrar una nueva compra
def registrarCompra(request):
    idCompra = request.POST["txtidcompra"]
    idProveedor = request.POST["txtidproveedor"]
    idEmpleado = request.POST["txtidempleado"]
    idProducto = request.POST["txtidproducto"]
    cantidad = request.POST["txtcantidad"]
    total = request.POST["txttotal"]
    fecha_compra = request.POST["txtfechacompra"]

    guardarCompra = Compras.objects.create(
        idCompra=idCompra,
        idprovedor=idProveedor,
        idEmpleado=idEmpleado,
        idProducto=idProducto,
        cantidad=cantidad,
        total=total,
        fecha_compra=fecha_compra
    )
    
    return redirect("Compras")

# Seleccionar una compra para editar
def seleccionarCompra(request, idCompra):
    compra = Compras.objects.get(idCompra=idCompra)
    return render(request, "editarcompra.html", {"laCompra": compra})

# Editar una compra existente
def editarCompra(request):
    idCompra = request.POST["txtidcompra"]
    idProveedor = request.POST["txtidproveedor"]
    idEmpleado = request.POST["txtidempleado"]
    idProducto = request.POST["txtidproducto"]
    cantidad = request.POST["txtcantidad"]
    total = request.POST["txttotal"]
    fecha_compra = request.POST["txtfechacompra"]

    compra = Compras.objects.get(idCompra=idCompra)
    compra.idprovedor = idProveedor
    compra.idEmpleado = idEmpleado
    compra.idProducto = idProducto
    compra.cantidad = cantidad
    compra.total = total
    compra.fecha_compra = fecha_compra
    compra.save()  # Guarda los cambios

    return redirect("Compras")

# Eliminar una compra
def borrarCompra(request, idCompra):
    compra = Compras.objects.get(idCompra=idCompra)
    compra.delete()  # Elimina el registro
    return redirect("Compras")
