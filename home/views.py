from django.shortcuts import render, HttpResponse, redirect
from .models import Producto

# Create your views here.

def ventaView(request):
    return render(request, 'home/venta.html')

def inventarioView(request):
    return render (request, 'home/inventario.html' )

def pqrsView(request):
    return render (request, 'home/pqrs.html')

def productosView(request):
    productoslistados = Producto.objects.all()
    return render (request, 'home/gestionProductos.html', {"productos": productoslistados})

def registrarProducto(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    precio=request.POST['numPrecio']

    producto=Producto.objects.create(
        codigo=codigo, nombre=nombre, precio=precio)
    return redirect('/home/productos')