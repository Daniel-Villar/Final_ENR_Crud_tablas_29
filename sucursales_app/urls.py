from django.urls import path
from . import views

urlpatterns = [
    path('Sucursal', views.inicio_vistaSucursales, name='Sucursal'),
    path('registrarSucursales/', views.registrarSucursales, name='registrarSucursales'),
    path('seleccionarSucursales/<str:idSucursales>/', views.seleccionarSucursales, name='seleccionarSucursales'),
    path('editarSucursales/', views.editarSucursales, name='editarSucursales'),
    path('borrarSucursales/<str:idSucursales>/', views.borrarSucursales, name='borrarSucursales'),
]
