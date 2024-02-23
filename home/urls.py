from django.urls import path
from .views import ventaView
from .views import inventarioView
from .views import pqrsView

urlpatterns = [
    path('venta', ventaView, name='venta'),
    path('inventario', inventarioView, name='inventario'),
    path('pqrs', pqrsView, name='pqrs' )

]
