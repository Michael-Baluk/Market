from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length= 250)
    precio = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.nombre
    
    class Meta:
     db_table = 'productos'
# Create your models here.
