from django.shortcuts import render, HttpResponse, redirect
from .models import Producto

# Create your views here.

def ventaView(request):
    return render(request, 'home/venta.html')

def inventarioView(request):
    return render (request, 'home/inventario.html' )

def pqrsView(request):
    pqrslistados = pqrs.objects.all()
    return render (request, 'home/pqrs.html', {"pqrs": pqrslistados})

def registrarpqrs(request):
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    tipo=request.POST['txttipo']
    mensaje=request.POST['txtmensaje']

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

def edicionProducto(request, codigo):
    producto= Producto.objects.get(codigo=codigo)
    return render(request, "edicionProducto.html", {"producto": producto})


def editarProducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.precio = precio
    producto.save()

    return redirect('/home/productos')

def eliminarProducto(request, codigo):
     producto=Producto.objects.get(codigo=codigo)
     producto.delete()
     
     return redirect('/home/productos')
 

 
 
     
     
    
