from django.db import models
from modelos.productos import Productos


class Pedidos(models.Model):
    cantidad = models.IntegerField("cantidad de productos", null=False, blank=False)
    precio = None
    producto = models.ForeignKey(Productos)
    fecha = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{}, {}, {}, {}".format(self.cantidad, self.precio, self.producto, self.fecha)
    

    class Meta:
        ordering = ["producto"]
        verbose_name_plural = "Mis pedidos"
