from django.db import models

# Create your models here.
class Alumno(models.Model):
    CARRERAS = [
        ('INFORMATICA', 'Informática'),
        ('ADMINISTRACION', 'Administración'),
        ('MECANICA', 'Mecánica'),
        ('CONSTRUCCION', 'Construcción'),
        ('ROBOTICA', 'Robótica'),
        ('CONTABILIDAD', 'Contabilidad'),
    ]

    nombre = models.CharField(max_length=100)
    nota1 = models.DecimalField(max_digits=3, decimal_places=1)
    nota2 = models.DecimalField(max_digits=3, decimal_places=1)
    nota3 = models.DecimalField(max_digits=3, decimal_places=1)
    fecha_ingreso = models.DateField()
    carrera = models.CharField(max_length=20, choices=CARRERAS)

    def __str__(self):
        return self.nombre