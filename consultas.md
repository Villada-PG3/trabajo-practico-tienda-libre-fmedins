1) Producto.objects.all()
2) Producto.objects.filter(precio__gt=50000)
3) Producto.objects.filter(precio__lt=50000)
4) Producto.objects.filter(nombre__icontains="kit")
5) Producto.objects.exclude(precio__lt=100000)
6) Producto.objects.order_by("precio")
7) Producto.objects.order_by("-precio")
8) Producto.objects.filter(precio__gte=390000)
9) Producto.objects.get(id=1)
10) producto = Producto.objects.get(id=1)
    producto.categoria

    categoria = producto.categoria
    categoria.productos.all()