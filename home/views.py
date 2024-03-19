from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .decorators import *
from .models import *
from django.core.mail import send_mail
from django.http import JsonResponse
import json
from django.utils import timezone
from datetime import datetime

@admin_required
def productos_mas_vendidos(request):
    productos_mas_vendidos = VentaProducto.objects.values('producto__nombre').annotate(total_vendido=models.Sum('cantidad')).order_by('-total_vendido')[:10]
    
    # Obtener el precio unitario para cada producto más vendido
    for producto in productos_mas_vendidos:
        nombre_producto = producto['producto__nombre']
        producto_obj = Producto.objects.get(nombre=nombre_producto)
        producto['precio_unitario'] = producto_obj.precio
    
    return render(request, 'home/productos_mas_vendidos.html', {'productos_mas_vendidos': productos_mas_vendidos})

@admin_required
def lista_venta(request):
    mes = request.GET.get('mes')
    ventas = Venta.objects.all()

    if mes:
        try:
            mes_numero = int(mes)
            # Obtener el primer día del mes
            fecha_inicio_mes = datetime(timezone.now().year, mes_numero, 1)
            # Obtener el último día del mes
            fecha_fin_mes = fecha_inicio_mes.replace(month=mes_numero % 12 + 1, day=1) - timezone.timedelta(days=1)
            # Filtrar las ventas dentro de este rango de fechas
            ventas = ventas.filter(fecha__range=[fecha_inicio_mes, fecha_fin_mes])
        except ValueError:
            messages.error(request, 'Mes inválido')

    return render(request, 'lista_venta.html', {'ventas': ventas})

@logout_required
def inicio(request):
    return render(request, 'inicio.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contraseña = request.POST.get('contraseña')
        user = Usuario.objects.filter(email=email, contraseña=contraseña).first()
        if user is not None:
            if user.idRol.id == 1:
                request.session['sesion'] = 1
                return redirect('dashAdmin')
            elif user.idRol.id == 2:
                request.session['sesion'] = 2
                return redirect('venta')
            else:
                return render(request, 'error_rol_desconocido.html')
        else:
            messages.error(request, 'Credenciales inválidas')

    return render(request, 'login.html')

def cerrar_sesion(request):
    if 'sesion' in request.session:
        del request.session['sesion']
    
    response = redirect('inicio')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

@admin_required
def dashAdmin(request):
    return render(request, 'dashboardAdmin.html')

@admin_required
def detalles_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    detalles_venta = VentaProducto.objects.filter(venta=venta)
    return render(request, 'detalles_venta.html', {'venta': venta, 'detalles_venta': detalles_venta})

@admin_required
def productosView(request):
    productoslistados = Producto.objects.all()
    return render(request, 'home/gestionProductos.html', {"productos": productoslistados})

@admin_required
def registrarProducto(request):
    if request.method == "POST":
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        precio = request.POST['numPrecio']
        stock = request.POST['numStock']

        if Producto.objects.filter(codigo=codigo).exists():
            messages.error(request, 'El código ingresado ya existe en la base de datos.')
            return redirect('/home/productos')

        if Producto.objects.filter(nombre__iexact=nombre).exists():
            messages.error(request, 'Este producto ya existe en la base de datos. Edita el precio o el stock en la tabla.')
            return redirect('/home/productos')

        Producto.objects.create(codigo=codigo, nombre=nombre, precio=precio, stock=stock)
        return redirect('/home/productos')

    return render(request, 'home/productos')

@admin_required
def edicionProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    return render(request, "home/edicionProducto.html", {"producto": producto})

@admin_required
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

@admin_required
def eliminarProducto(request, codigo):
     producto=Producto.objects.get(codigo=codigo)
     producto.delete()
     return redirect('/home/productos')

@vendedor_required
def ventaView(request):
    productosListados = Producto.objects.all()
    return render(request, 'home/gestionVenta.html', {"producto": productosListados})

def pqrsView(request):
    pqrslistados = Pqrs.objects.all()
    return render (request, 'home/pqrs.html', {"pqrs": pqrslistados}) 


def registrarPqrs(request):
    nombre=request.POST['txtnombre']
    correo=request.POST['txtcorreo']
    telefono=request.POST['txttelefono']
    tipoPqrs=request.POST['txttipoPqrs']
    mensaje=request.POST['txtmensaje']
    
    pqrs=Pqrs.objects.create(
        nombre=nombre, correo=correo, telefono = telefono ,tipoPqrs=tipoPqrs, mensaje=mensaje)
    return redirect('/home')
@admin_required
def eliminarPqrs(request, codigo):
     pqrs=Pqrs.objects.get(codigo=codigo)
     pqrs.delete()
     
     return redirect('/home/lista_pqrs')
@admin_required
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
        pqrs.estado = "Respondida" 
        pqrs.save()

        asunto = 'Respuesta PQRS'
        mensaje_respuesta = f'Tu PQRS ha sido respondido: \n{respuesta}'
        mensaje_original = f'Tu PQRS registrada\nFecha: {pqrs.fecha}\nMensaje: {pqrs.mensaje}'

        try:
            enviar_correo_respuesta(pqrs.correo, asunto, mensaje_original + '\n\n' + mensaje_respuesta)
            return redirect('dashboardPQRS')
        except Exception as e:
            print(f'Error al enviar el correo: {str(e)}')

    return render(request, 'dashboardPQRS.html', {"pqrs_list": Pqrs.objects.all()})

@admin_required
def lista_stock(request):
    stock = Stock.objects.all() 
    productos = Producto.objects.all()
    stock_con_nombre_producto = []

    # Agregar el nombre del producto a cada entrada de stock
    for item in stock:
        producto = productos.filter(codigo=item.producto_codigo).first()
        stock_con_nombre_producto.append({
            'producto_nombre': producto.nombre,
            'cantidad': item.cantidad,
            'fecha': item.fecha
        })

    return render(request, 'lista_stock.html', {'stock': stock_con_nombre_producto})

@admin_required
def edicionStock(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    return render(request, "home/edicionStock.html", {"producto": producto})

@admin_required
def editarStockProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    if request.method == 'POST':
        stock_nuevo = int(request.POST['numStock'])
        producto.stock += stock_nuevo
        producto.save()
        Stock.objects.create(producto_codigo=producto.codigo, cantidad=stock_nuevo)
        return redirect('/home/productos')

    return render(request, "home/edicionStock.html", {"producto": producto})

@vendedor_required
def guardar_arrays(request):
    if request.method == "POST":
        data = json.loads(request.body)
        productos = data.get("productos", [])
        cantidades = data.get("cantidades", [])
        total_general = data.get("totalGeneral", 0)

        venta = Venta.objects.create(total_venta=total_general)

        total_venta = 0
        for producto_id, cantidad in zip(productos, cantidades):
            producto = Producto.objects.get(codigo=producto_id)
            total_venta += producto.precio * cantidad
            venta_producto = VentaProducto.objects.create(
                venta=venta,
                producto=producto,
                cantidad=cantidad
            )
            producto.stock -= cantidad
            producto.save()

        venta.total_venta = total_venta
        venta.save()

        return JsonResponse({"venta_id": venta.pk})
    else:
        return JsonResponse({"error": "Método no permitido."}, status=405)

@vendedor_required    
def ticket_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    productos_venta = VentaProducto.objects.filter(venta=venta)
    context = {
        'venta': venta,
        'productos_venta': productos_venta,
    }
    return render(request, 'home/ticket_venta.html', context)

@vendedor_required
def cobro_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)

    if request.method == 'POST':
        venta_codigo = request.POST.get('venta_codigo')
        monto_pagado = request.POST.get('monto_pagado')
        total_venta = venta.total_venta
        cambio = float(monto_pagado) - total_venta
        return JsonResponse({'cambio': cambio})

    else:
        context = {
            'venta': venta
        }
        return render(request, 'home/cobro_venta.html', context)

@vendedor_required    
def obtener_total_venta(request, venta_codigo):
    venta = Venta.objects.get(codigo=venta_codigo)
    total_venta = venta.total_venta
    return JsonResponse({'total_venta': total_venta})

@admin_required
def editarStockProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    if request.method == 'POST':
        stock_nuevo = int(request.POST['numStock'])
        producto.stock += stock_nuevo
        producto.save()
        Stock.objects.create(producto_codigo=producto.codigo, cantidad=stock_nuevo)
        return redirect('/home/productos')

    return render(request, "home/edicionStock.html", {"producto": producto})
