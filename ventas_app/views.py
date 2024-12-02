from django.shortcuts import render,redirect
from .models import Ventas

# Create your views here.
def inicio_vistaVentas(request):
    lasVentas=Ventas.objects.all()
    return render(request,"gestionarventas.html",{"LasVentas2":lasVentas})

def registrarVentas(request):
    idVentas =request.POST["txtidventas"]
    idEmpleado =request.POST["txtidempleado"]
    idCliente  =request.POST["txtcliente"]
    idProductos =request.POST["txtidproducto"]
    idSucursal =request.POST["txtsucursal"]
    fecha_venta  =request.POST["txtfecha_venta"]
    cantidad =request.POST["txtcantidad"]
    total =request.POST["txttotal"]
    

    guardarVentas=Ventas.objects.create(
        idVentas=idVentas,
        idEmpleado=idEmpleado,
        idCliente=idCliente,
        idProductos=idProductos,
        idSucursal=idSucursal,
        fecha_venta=fecha_venta,
        cantidad=cantidad,
        total=total
        
    ) # Guarda el Registro

    return redirect("Venta")

def seleccionaVentas(request, idVentas):
    venta = Ventas.objects.get(idVentas=idVentas)
    return render(request, "editarventas.html", {"venta": venta})

def editarVentas(request):
    idVentas =request.POST["txtidventas"]
    idEmpleado =request.POST["txtidempleado"]
    idCliente  =request.POST["txtcliente"]
    idProductos =request.POST["txtidproducto"]
    idSucursal =request.POST["txtsucursal"]
    fecha_venta  =request.POST["txtfecha_venta"]
    cantidad =request.POST["txtcantidad"]
    total =request.POST["txttotal"]
    ventas=Ventas.objects.get(idVentas=idVentas)
    ventas.idEmpleado=idEmpleado
    ventas.idCliente=idCliente
    ventas.idProductos=idProductos
    ventas.idSucursal=idSucursal
    ventas.fecha_venta=fecha_venta
    ventas.cantidad=cantidad
    ventas.total=total
    ventas.save() #Guarda Registro Actualizado
    return redirect("Venta")

def borrarVentas(request,idVentas):
    venta=Ventas.objects.get(idVentas=idVentas)
    venta.delete() #Borra el Registro
    return redirect("Venta")