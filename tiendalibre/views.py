from django.shortcuts import render


def home(request):
    productos = [
        {
            "nombre": "Notebook Lenovo",
            "precio": 850000,
            "stock": 5
        },
        {
            "nombre": "Mouse Logitech",
            "precio": 25000,
            "stock": 10
        },
        {
            "nombre": "Teclado Redragon",
            "precio": 45000,
            "stock": 0
        },
        {
            "nombre": "Monitor Samsung",
            "precio": None,
            "stock": 3
        },
        {
            "nombre": "Auriculares HyperX",
            "precio": 75000,
            "stock": 7
        },
        {
            "nombre": "Disco Duro Externo Seagate",
            "precio": 150000,
            "stock": 2
        },
    ]

    contexto = {
        "titulo": "Ofertas",
        "usuario_logeado": request.user.is_authenticated,
        "productos": productos,
    }

    return render(request, "tiendalibre/home.html", contexto)


def acerca_de_mi(request):
    return render(request, "tiendalibre/acercaDeMi.html")