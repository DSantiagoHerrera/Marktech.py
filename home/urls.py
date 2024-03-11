from django.urls import path
from . import views

urlpatterns = [
    path('pqrs/', views.pqrsView, name='pqrs' ),
    path('registrarPqrs/', views.registrarPqrs),
    path('eliminarPqrs/<codigo>/', views.eliminarPqrs),
    path('productos/', views.productosView, name='productos'),
    path('registrarProducto/', views.registrarProducto),
    path('edicionProducto/<codigo>/', views.edicionProducto),
    path('editarProducto/<codigo>/', views.editarProducto),
    path('eliminarProducto/<codigo>/', views.eliminarProducto),
    path('lista_pqrs/', views.lista_pqrs, name='lista_pqrs'),
    path('dashboardPQRS/', views.dashboardPQRS, name='dashboardPQRS'),
    path('home/responder_pqrs/<int:codigo>/', views.responder_pqrs, name='responder_pqrs'),
    path('', views.inicio, name='home'),
    path('redireccion/', views.redireccion, name ='redireccion'),
    path('venta', views.ventaView, name='venta'),
    path('edicionStock/<codigo>/', views.edicionStock),
    path('editarStockProducto/<codigo>/', views.editarStockProducto, name='editar_stock_producto'),
    path('guardar_arrays/', views.guardar_arrays, name='guardar_arrays'),
    path('ticket_venta/<int:venta_id>/', views.ticket_venta, name='ticket_venta'),
    path('cobro_venta/<int:venta_id>/', views.cobro_venta, name='cobro_venta'),
    path('obtener_total_venta/<int:venta_codigo>/', views.obtener_total_venta, name='obtener_total_venta'),
]
