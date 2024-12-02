from django.urls import path
from ventas_app import views

urlpatterns = [
    path('Venta', views.inicio_vistaVentas, name='Venta'),
    path('registrarVentas/', views.registrarVentas, name='registrarVentas'),
    path('seleccionaVentas/<int:idVentas>/', views.seleccionaVentas, name='seleccionaVentas'),
    path('editarVentas/', views.editarVentas, name='editarVentas'),
    path('borrarVentas/<int:idVentas>/', views.borrarVentas, name='borrarVentas'),
]