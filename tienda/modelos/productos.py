from django.db import models


# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(max_length=800, null=False)
    precio = models.FloatField(verbose_name="precio producto", null=False)
    imagen = models.ImageField(upload_to="media/productos")

    def __str__(self):
        return self.nombre
    

    @property
    def pass_():
        pass
    

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Mis productos"
