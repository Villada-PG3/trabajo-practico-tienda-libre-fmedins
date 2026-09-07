from django.shortcuts import render
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