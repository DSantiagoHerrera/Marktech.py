from django.shortcuts import render, HttpResponse

# Create your views here.

def ventaView(request):
    return render(request, 'home/venta.html')

def inventarioView(request):
    return render (request, 'home/inventario.html' )

def pqrsView(request):
    return render (request, 'home/pqrs.html')