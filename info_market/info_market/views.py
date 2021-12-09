from django.shortcuts import render
from django.views.generic import TemplateView
from apps.productos.models import Producto


""" vista basada en funcion
def inicio(request):

    context = {
        'productos': Producto.objects.all()
    }

    return render(request, 'inicio.html', context)

"""
class Inicio(TemplateView):
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context["productos_a"] = Producto.objects.all() 
        return context
    
