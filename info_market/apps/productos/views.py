from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Producto
from .forms import ProductoForm
from django.urls import reverse_lazy
# Create your views here.
def detalle(request):
    context = {}
    return render(request, 'productos/detalle.html', context)

class ListarAdmin(ListView):
    template_name = 'productos/admin/listar.html'
    model = Producto
    context_object_name = "productos"

class AdminNuevo(CreateView):
    template_name = 'productos/admin/nuevo.html'
    model = Producto
    form_class = ProductoForm


    def get_success_url(self, **kwargs):
        return reverse_lazy("productos:admin_nuevo")
