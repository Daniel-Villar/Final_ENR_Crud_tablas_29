from django.shortcuts import render,redirect
from .models import Clientes
# Create your views here.

# Create your views here.
def inicio_vistaCliente(request):
    losclienetes=Clientes.objects.all()
    return render(request,"gestionarcliente.html",{"losclientes2":losclienetes})

def registrarClientes(request):
    idCliente=request.POST["txtidCliente"]
    nombre=request.POST["txtnombre"]
    Fecha_nac=request.POST["txtFecha_nac"]
    sexo=request.POST["txtSexo"]
    no_telefono=request.POST["txtTelefono"]
    Direccion=request.POST["txtDireccion"]
    email=request.POST["txtEmail"]

    guardarClientes=Clientes.objects.create(
        idCliente=idCliente,
        nombre=nombre,
        Fecha_nac=Fecha_nac,
        sexo=sexo,
        no_telefono=no_telefono,
        Direccion=Direccion,
        email=email
    ) # Guarda el Registro

    return redirect("Cliente")

def seleccionarClientes(request,idCliente):
    cliente=Clientes.objects.get(idCliente=idCliente)
    return render(request, "editarcliente.html", {"losclientes2": cliente})


def editarClientes(request):
    idCliente=request.POST["txtidCliente"]
    nombre=request.POST["txtnombre"]
    Fecha_nac=request.POST["txtFecha_nac"]
    sexo=request.POST["txtSexo"]
    no_telefono=request.POST["txtTelefono"]
    Direccion=request.POST["txtDireccion"]
    email=request.POST["txtEmail"]
    cliente=Clientes.objects.get(idCliente=idCliente)
    cliente.nombre=nombre
    cliente.Fecha_nac=Fecha_nac
    cliente.sexo=sexo
    cliente.no_telefono=no_telefono
    cliente.Direccion=Direccion
    cliente.email=email
    cliente.save() #Guarda Registro Actualizado
    return redirect("Cliente")

def borrarClientes(request,idCliente):
    cliente=Clientes.objects.get(idCliente=idCliente)
    cliente.delete() #Borra el Registro
    return redirect("Cliente")