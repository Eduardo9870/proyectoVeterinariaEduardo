from django.db import models

# Create your models here.

class Mascotas (models.Model):
    nombre = models.CharField(max_length=50)
    fechaAtencion = models.DateField(null=True, blank=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField()
    edad = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    nombreDueño = models.CharField(max_length=50)
    apellidoDueño = models.CharField(max_length=50)
    emailDueño = models.EmailField()

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
    def __str__(self):
        return self.nombre
    def __str__(self):
        return self.nombreDueño
    def __str__(self):
        return self.fechaAtencion

