from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
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
    ordering = ["pk"]
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()

        busqueda = self.request.GET.get("q", "").strip()

        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) |
                Q(marca__icontains=busqueda) |
                Q(descripcion__icontains=busqueda)
            )

        return queryset

class CategoriaView(ListView):
    model = Producto
    template_name = "tiendalibre/categoria.html"
    context_object_name = "productos"

    def get_queryset(self):
        return Producto.objects.filter(
            categoria__slug=self.kwargs["slug"]
        )


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "tiendalibre/detalle.html"
    context_object_name = "producto"
