from django.urls import path
from . import views

urlpatterns = [
    path('pqrs/', views.pqrsView, name='pqrs' ),
    path('registrarPqrs/', views.registrarPqrs),
    path('productos/', views.productosView, name='productos'),
    path('registrarProducto/', views.registrarProducto),
    path('edicionProducto/<codigo>/', views.edicionProducto),
    path('editarProducto/<codigo>/', views.editarProducto),
    path('eliminarProducto/<codigo>/', views.eliminarProducto),
    path('lista_pqrs/', views.lista_pqrs, name='lista_pqrs'),
    path('', inicio, name='home'),
    path('redireccion/', redireccion, name ='redireccion'),
    path('venta', ventaView, name='venta'),
    path('registrarVenta/', registrarVenta),
    path('edicionVenta/<codigo>', edicionVenta),
    path('editarVenta/<codigo>', editarVenta),
    path('eliminarVenta/<codigo>', eliminarVenta),
]
