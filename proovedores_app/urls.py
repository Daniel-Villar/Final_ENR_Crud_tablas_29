from django.urls import path
from proovedores_app import views

urlpatterns = [
    path("Proveedor", views.inicio_vistaProveedor, name="Proveedor"),
    path("registrarProveedores/", views.registrarProveedores, name="registrarProveedores"),
    path("seleccionarProveedores/<idProveedor>", views.seleccionarProveedores, name="seleccionarProveedores"),
    path("editarProveedores/", views.editarProveedores, name="editarProveedores"),
    path("borrarProveedores/<idProveedor>", views.borrarProveedores, name="borrarProveedores"),
]
