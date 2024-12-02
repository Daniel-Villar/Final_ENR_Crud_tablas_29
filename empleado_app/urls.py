from django.urls import path
from empleado_app import views

urlpatterns = [
    path("Empleado", views.inicio_vistaEmpleado, name="Empleado"),
    path("registrarEmpleados/", views.registrarEmpleados, name="registrarEmpleados"),
    path("seleccionarEmpleados/<idEmpleado>", views.seleccionarEmpleados, name="seleccionarEmpleados"),
    path("editarEmpleados/", views.editarEmpleados, name="editarEmpleados"),
    path("borrarEmpleados/<idEmpleado>", views.borrarEmpleados, name="borrarEmpleados"),
]