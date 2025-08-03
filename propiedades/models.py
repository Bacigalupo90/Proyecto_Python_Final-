
from django.db import models
from django.utils import timezone

class Propiedad(models.Model):
    
    titulo = models.CharField(max_length=200, verbose_name="Título de la Propiedad")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio (USD)")
    imagen = models.ImageField(upload_to='propiedades/', null=True, blank=True, verbose_name="Imagen")
    fecha_publicacion = models.DateField(default=timezone.now, verbose_name="Fecha de Publicación")

    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
        ordering = ['-fecha_publicacion'] 

    def __str__(self):
        return self.titulo

