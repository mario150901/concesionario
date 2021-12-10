from django.db import models

# Create your models here.
class Coche(models.Model):

    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    combustible = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    fabricante = models.ForeignKey('Fabricante', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.marca and self.modelo

class Fabricante(models.Model):

    nombre_fabricante = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_fabricante