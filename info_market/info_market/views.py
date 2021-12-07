from django.shortcuts import render
from apps.productos.models import Producto


def inicio(request):

    productos = Producto.objects.all()
    usuario = {
        'nombre': 'Maikel',
        'apellido': 'Baluk'
    }

    context = {
        'usuario': usuario,
        'productos': productos ,
    }

    return render(request, 'inicio.html', context)

def login(request):
    print("========")
    print(request.POST.get("password",))
    return render(request, 'login.html')
