from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
path('detalle/', views.detalle, name = "detalle"),
path('Admin/listar', views.ListarAdmin.as_view(), name = "admin_listar"),
path('Admin/nuevo',views.AdminNuevo.as_view(), name= 'admin_nuevo'),
path('Admin/editar/<int:pk>/',views.EditarAdmin.as_view(), name= "admin_editar"),
path('Admin/eliminar/<int:pk>/',views.AdminEliminar.as_view(), name= "admin_eliminar"),
]