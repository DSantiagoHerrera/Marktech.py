from django.urls import path
from .views import *

urlpatterns = [
    path('venta', ventaView, name='venta'),
    path('inventario', inventarioView, name='inventario'),
    path('pqrs', pqrsView, name='pqrs' ),
    path('productos', productosView, name='productos'),
    path('registrarProducto/', registrarProducto),
    path('edicionProducto/<codigo>', edicionProducto),
    path('editarProducto/', editarProducto),
    path('eliminarProducto/<codigo>', eliminarProducto)

]
