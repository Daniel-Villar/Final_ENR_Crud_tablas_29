from django.shortcuts import render,redirect
from .models import Productos

# Create your views here.
def inicio_vistaProductos(request):
    losProductos=Productos.objects.all()
    return render(request,"gestionarproducto.html",{"losProductos2":losProductos})

def registrarProductos(request):
    idProducto =request.POST["txtidproducto"]
    nombre=request.POST["txtnombre"]
    Precio=request.POST["txtprecio"]
    descripcion=request.POST["txtdescripcion"]
    precio_mayoreo=request.POST["txtprecio_mayoreo"]
    stock=request.POST["txtstock"]
    demanda=request.POST["txtdemanda"]
    idSucursal=request.POST["txtidsucursal"]

    guardarProductos=Productos.objects.create(
        idProducto=idProducto,
        nombre=nombre,
        Precio=Precio,
        descripcion=descripcion,
        precio_mayoreo=precio_mayoreo,
        stock=stock,
        demanda=demanda,
        idSucursal=idSucursal
    ) # Guarda el Registro

    return redirect("Producto")

def seleccionarProductos(request, idProducto):
    producto = Productos.objects.get(idProducto=idProducto)
    return render(request, "editarproducto.html", {"losProductos": producto})


def editarProductos(request):
    idProducto =request.POST["txtidproducto"]
    nombre=request.POST["txtnombre"]
    Precio=request.POST["txtprecio"]
    descripcion=request.POST["txtdescripcion"]
    precio_mayoreo=request.POST["txtprecio_mayoreo"]
    stock=request.POST["txtstock"]
    demanda=request.POST["txtdemanda"]
    idSucursal=request.POST["txtidsucursal"]
    productos=Productos.objects.get(idProducto=idProducto)
    productos.nombre=nombre
    productos.Precio=Precio
    productos.descripcion=descripcion
    productos.precio_mayoreo=precio_mayoreo
    productos.stock=stock
    productos.demanda=demanda
    productos.idSucursal=idSucursal
    productos.save() #Guarda Registro Actualizado
    return redirect("Producto")

def borrarProductos(request,idProducto):
    productos=Productos.objects.get(idProducto=idProducto)
    productos.delete() #Borra el Registro
    return redirect("Producto")