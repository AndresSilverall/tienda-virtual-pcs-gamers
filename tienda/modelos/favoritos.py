from django.db import models
from modelos.productos import Productos


class Favoritos(models.Model):
    producto = models.ManyToManyField(Productos)


    def __str__(self):
        return self.producto