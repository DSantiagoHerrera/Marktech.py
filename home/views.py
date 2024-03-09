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

def guardar_arrays(request):
    if request.method == "POST":
        data = json.loads(request.body)
        productos = data.get("productos", [])
        cantidades = data.get("cantidades", [])
        total_general = data.get("totalGeneral", 0)

        # Crear una instancia de Venta
        venta = Venta.objects.create(total_venta=total_general)

        # Calcular el total de la venta y actualizar la instancia de Venta
        total_venta = 0
        for producto_id, cantidad in zip(productos, cantidades):
            producto = Producto.objects.get(codigo=producto_id)
            total_venta += producto.precio * cantidad
            # Crear una instancia de VentaProducto y asociarla a la venta
            venta_producto = VentaProducto.objects.create(
                venta=venta,
                producto=producto,
                cantidad=cantidad
            )
            # Actualizar el stock del producto
            producto.stock -= cantidad
            producto.save()

        venta.total_venta = total_venta
        venta.save()

        return JsonResponse({"venta_id": venta.pk})
    else:
        return JsonResponse({"error": "Método no permitido."}, status=405)
    
def ticket_venta(request, venta_id):
    # Obtener la instancia de la venta
    venta = get_object_or_404(Venta, pk=venta_id)

    # Obtener los productos asociados a la venta
    productos_venta = VentaProducto.objects.filter(venta=venta)

    # Pasar la información a la plantilla del ticket
    context = {
        'venta': venta,
        'productos_venta': productos_venta,
    }

    # Renderizar la plantilla del ticket
    return render(request, 'home/ticket_venta.html', context)

def cobro_venta(request):
    if request.method == 'POST':
        venta_codigo = request.POST.get('venta_codigo')
        monto_pagado = request.POST.get('monto_pagado')

        venta = get_object_or_404(Venta, codigo=venta_codigo)
        total_venta = venta.total_venta

        cambio = float(monto_pagado) - total_venta

        return JsonResponse({'cambio': cambio})
    else:
        return render(request, 'home/cobro_venta.html')
    
def obtener_total_venta(request, venta_codigo):
    venta = Venta.objects.get(codigo=venta_codigo)
    total_venta = venta.total_venta
    return JsonResponse({'total_venta': total_venta})










 
 
     
     
    
