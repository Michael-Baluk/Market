from django.shortcuts                        import render
from django.views.generic                    import ListView, CreateView, UpdateView
from django.views.generic.edit               import UpdateView, DeleteView, FormView
from .models                                 import Producto
from .forms                                  import ProductoForm
from django.urls                             import reverse_lazy
from django.contrib.auth.decorators          import user_passes_test
from apps.Usuarios.mixins                    import SuperUsuarioMixin
# Create your views here.

def detalle(request):
    context = {}
    return render(request, 'productos/detalle.html', context)

class ListarAdmin(SuperUsuarioMixin,ListView):
    template_name = 'productos/admin/listar.html'
    model = Producto
    context_object_name = "productos"

    def get_queryset(self):
        return Producto.objects.all().order_by("id")
    

class AdminNuevo(SuperUsuarioMixin,CreateView):
    template_name = 'productos/admin/nuevo.html'
    model = Producto
    form_class = ProductoForm


    def get_success_url(self, **kwargs):
        return reverse_lazy("productos:admin_nuevo")

class EditarAdmin(SuperUsuarioMixin,UpdateView):
    template_name = 'productos/admin/editar.html'
    model = Producto
    form_class = ProductoForm


    def get_success_url(self, **kwargs):
        return reverse_lazy("productos:admin_listar")

class AdminEliminar(SuperUsuarioMixin,DeleteView):
    template_name = 'productos/admin/eliminar.html'
    model = Producto
    success_url = reverse_lazy('productos:admin_listar')
