from django.urls import path
from productos_app import views

urlpatterns = [
    path('Producto', views.inicio_vistaProductos, name='Producto'),
    path('registrarProductos/', views.registrarProductos, name='registrarProductos'),
    path('seleccionarProductos/<int:idProducto>/', views.seleccionarProductos, name='seleccionarProductos'),
    path('editarProductos/', views.editarProductos, name='editarProductos'),
    path('borrarProductos/<int:idProducto>/', views.borrarProductos, name='borrarProductos'),
]