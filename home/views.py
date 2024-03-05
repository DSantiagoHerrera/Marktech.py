from django.shortcuts import render, HttpResponse, redirect
from .models import Producto, Pqrs

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def redireccion (request):
    return render (request, 'redireccion.html')
    
def pqrsView(request):
    pqrslistados = Pqrs.objects.all()
    return render (request, 'home/pqrs.html', {"pqrs": pqrslistados})

def lista_pqrs(request):
    pqrs_list = Pqrs.objects.all() 
    return render(request, 'lista_pqrs.html', {'pqrs_list': pqrs_list})

def registrarPqrs(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    correo=request.POST['txtcorreo']
    tipoPqrs=request.POST['txttipoPqrs']
    mensaje=request.POST['txtmensaje']
    
    pqrs=Pqrs.objects.create(
        codigo=codigo, nombre=nombre, correo=correo, tipoPqrs=tipoPqrs, mensaje=mensaje)
    return redirect('/home/pqrs')

def eliminarPqrs(request, codigo):
     pqrs=Pqrs.objects.get(codigo=codigo)
     pqrs.delete()
     
     return redirect('/home/lista_pqrs')
    

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
    return render(request, "home/edicionProducto.html", {"producto": producto})


def editarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        precio = request.POST['numPrecio']

        producto.nombre = nombre
        producto.precio = precio
        producto.save()

        return redirect('/home/productos')

    return render(request, "home/edicionProducto.html", {"producto": producto})


def eliminarProducto(request, codigo):
     producto=Producto.objects.get(codigo=codigo)
     producto.delete()
     
     return redirect('/home/productos')
 
#Venta ---------------------------------------------------------------------------------------------------------------------


def ventaView(request):
    productosListados = Producto.objects.all()
    return render(request, 'home/gestionVenta.html', {"producto": productosListados})


    '''
    ventalistada = Venta.objects.all()
    return render (request, 'home/gestionVenta.html', {"venta": ventalistada})
    '''

def registrarVenta(request):
    if request.method == 'POST':
        productos_seleccionados = request.POST.getlist('productos')
        productos_seleccionados = Producto.objects.filter(codigo__in=productos_seleccionados)
        total_venta = sum(producto.precio for producto in productos_seleccionados)
        venta = Venta(totalVenta=total_venta)
        venta.save()
        venta.productos.add(*productos_seleccionados)
        return redirect('pagina_de_confirmacion')
    else:
        productos = Producto.objects.all()
        return render(request, 'home/gestionVenta.html', {'productos': productos})

def edicionVenta(request, codigo):
    venta = Venta.objects.get(codigo=codigo)
    return render(request, "home/edicionVenta.html", {"venta": venta})


def editarVenta(request, codigo):
    venta = Venta.objects.get(codigo=codigo)
    if request.method == 'POST':
        productos = request.POST['txtProductos']
        totalVenta = request.POST['numTotalVenta']

        venta.productos = productos
        venta.totalVenta = totalVenta
        venta.save()

        return redirect('/home/venta')

    return render(request, "home/edicionVenta.html", {"venta": venta})


def eliminarVenta(request, codigo):
     producto=Producto.objects.get(codigo=codigo)
     producto.delete()
     
     return redirect('/home/venta')



 
 
     
     
    
