from django.shortcuts import render, HttpResponse, redirect
import smtplib
from django.core.mail import send_mail
from django.conf import settings
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
    nombre=request.POST['txtnombre']
    correo=request.POST['txtcorreo']
    telefono=request.POST['txttelefono']
    tipoPqrs=request.POST['txttipoPqrs']
    mensaje=request.POST['txtmensaje']
    
    pqrs=Pqrs.objects.create(
        nombre=nombre, correo=correo, telefono = telefono ,tipoPqrs=tipoPqrs, mensaje=mensaje)
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
    stock=request.POST['numStock']

    producto=Producto.objects.create(
        codigo=codigo, nombre=nombre, precio=precio, stock=stock)
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

def dashboardPQRS(request):
    pqrs_list = Pqrs.objects.all()
    return render(request, 'home/dashboardPQRS.html', {"pqrs_list": pqrs_list})


def enviar_correo_respuesta(correo, asunto, mensaje):
    try:
        send_mail(asunto, mensaje, 'panneecaffe2024@gmail.com', [correo])
        print(f'Correo enviado a {correo} con éxito.')
    except Exception as e:
        print(f'Error al enviar el correo: {str(e)}')


def responder_pqrs(request, codigo):
    pqrs = Pqrs.objects.get(codigo=codigo)

    if request.method == 'POST':
        respuesta = request.POST.get('txtrespuesta', '')
        pqrs.respuesta = respuesta
        pqrs.save()

        asunto = 'Respuesta PQRS'
        mensaje_respuesta = f'Tu PQRS ha sido respondido: {respuesta}'
        mensaje_original = f'Tu PQRS: {pqrs.mensaje}'

        try:
            enviar_correo_respuesta(pqrs.correo, asunto, mensaje_original + '\n\n' + mensaje_respuesta)
            return redirect('dashboardPQRS')
        except Exception as e:
            print(f'Error al enviar el correo: {str(e)}')

    return render(request, 'dashboardPQRS.html', {"pqrs_list": Pqrs.objects.all()})




def edicionStock(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    return render(request, "home/edicionStock.html", {"producto": producto})

def editarStockProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    if request.method == 'POST':
        stock_nuevo = int(request.POST['numStock'])
        producto.stock += stock_nuevo  # Suma la cantidad nueva al stock existente
        producto.save()
        return redirect('/home/productos')

    return render(request, "home/edicionStock.html", {"producto": producto})








 
 
     
     
    
