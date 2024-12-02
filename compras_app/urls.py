from django.urls import path
from compras_app import views

urlpatterns = [
    path("Compras", views.inicio_vistaCompras, name="Compras"),
    path("registrarCompra/", views.registrarCompra, name="registrarCompra"),
    path("seleccionarCompra/<idCompra>", views.seleccionarCompra, name="seleccionarCompra"),
    path("editarCompra/", views.editarCompra, name="editarCompra"),
    path("borrarCompra/<idCompra>", views.borrarCompra, name="borrarCompra"),
]
