from django.urls import path
from .views import *

urlpatterns = [
    path('pqrs', pqrsView, name='pqrs' ),
    path('registrarPqrs/', registrarPqrs),
    path('productos', productosView, name='productos'),
    path('registrarProducto/', registrarProducto),
    path('edicionProducto/<codigo>', edicionProducto),
    path('editarProducto/<codigo>', editarProducto),
    path('eliminarProducto/<codigo>', eliminarProducto)

]
