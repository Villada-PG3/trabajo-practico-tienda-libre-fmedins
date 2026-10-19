
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Producto


class HomeView(TemplateView):
    template_name = "tiendalibre/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["titulo"] = "Ofertas"
        context["usuario_logeado"] = self.request.user.is_authenticated
        context["productos"] = Producto.objects.order_by("-fecha_creacion")[:3]

        return context


def acerca_de_mi(request):
    return render(request, "tiendalibre/acercaDeMi.html")


class CatalogoView(ListView):
    model = Producto
    template_name = "tiendalibre/catalogo.html"
    context_object_name = "productos"


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    return render(request, "tiendalibre/detalle.html", {
        "producto": producto
    })
