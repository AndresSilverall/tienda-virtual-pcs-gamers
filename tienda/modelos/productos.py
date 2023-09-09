from django.db import models
from django.utils.text import slugify 
from django.urls import reverse


# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(max_length=800, null=False)
    precio = models.FloatField(verbose_name="precio producto", null=False)
    imagen = models.ImageField(upload_to="media/productos")
    slug = models.SlugField(max_length=500, default="", null=True)


    def __str__(self):
        return self.nombre


    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Productos, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("nombre_producto", kwargs={"slug": self.slug})

   
    @property
    def obtener_todos_los_datos():
        return Productos.objects.all()
    

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Mis productos"
