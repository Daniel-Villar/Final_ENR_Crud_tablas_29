from django.urls import path
from cliente_app import views

urlpatterns = [
    path("Cliente", views.inicio_vistaCliente, name="Cliente"),
    path("registrarClientes/", views.registrarClientes, name="registrarClientes"),
    path("seleccionarClientes/<idCliente>", views.seleccionarClientes, name="seleccionarClientes"),
    path("editarClientes/", views.editarClientes, name="editarClientes"),
    path("borrarClientes/<idCliente>", views.borrarClientes, name="borrarClientes"),
]