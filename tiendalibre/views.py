from django.shortcuts import render, get_object_or_404
from .models import Producto


def home(request):
    productos = Producto.objects.order_by('-fecha_creacion')[:3]

    contexto = {
        "titulo": "Ofertas",
        "usuario_logeado": request.user.is_authenticated,
        "productos": productos,
    }

    return render(request, "tiendalibre/home.html", contexto)


def acerca_de_mi(request):
    return render(request, "tiendalibre/acercaDeMi.html")

def catalogo(request):
    productos = Producto.objects.all()

    return render(request, 'tiendalibre/catalogo.html', {
        'productos': productos
    })

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'tiendalibre/detalle.html', {
        'producto': producto
    })