from django.db import models




class Habitacion(models.Model):
    TIPOS_ESTADO = [
        ('Disponible', 'Disponible'),
        ('Asignada', 'Asignada'),
        ('Mantenimiento', 'Mantenimiento')
    ]

    TIPOS_CAMA = [
        ('King', 'King'),
        ('Queen', 'Queen'),
        ('2 plazas', '2 plazas'),
        ('1 plaza', '1 plaza')
    ]

    numero_habitacion = models.IntegerField(unique=True)
    tipo_cama = models.CharField(max_length=50)
    accesorios = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=15, choices=TIPOS_ESTADO)

    def __str__(self):
        return f'Habitación {self.numero_habitacion} - {self.estado}'