from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
path('detalle/', views.detalle, name="detalle"),
path('Admin/listar', views.ListarAdmin.as_view(), name = "admin_listar"),
]