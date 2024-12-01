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
    tipo_cama = models.CharField(max_length=50, choices=TIPOS_CAMA)
    accesorios = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=15, choices=TIPOS_ESTADO)

    def __str__(self):
        return f'Habitación {self.numero_habitacion} - {self.estado}'
    


class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    rut_empresa = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_empresa
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.rut}'
    

class Comedor(models.Model):

    TIPOS_SERVICIOS = [
        ('Ejecutivo', 'Ejecutivo'),
        ('Especial', 'Especial'),
        ('General', 'General')
    ]
    
    nombre_plato = models.CharField(max_length=100)
    tipo_servicio = models.CharField(max_length=50, choices=TIPOS_SERVICIOS) 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre_plato
    

class Proveedor(models.Model):

    RUBROS = [
        ('Carniceria', 'Carniceria'),
        ('Verduleria', 'Verduleria'),
        ('Pescaderia', 'Pescaderia'),
        ('Tecnologia', 'Tecnologia'),
        ('Ferreteria', 'Ferreteria'),
        ('Articulos de Aseo', 'Articulos de Aseo')
    ]
    nombre_proveedor = models.CharField(max_length=100)
    rut_proveedor = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    rubro = models.CharField(max_length=20, choices=RUBROS)

    def __str__(self):
        return self.nombre_proveedor


class Venta(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    plato = models.ForeignKey('Comedor', on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Venta: {self.cliente.nombre} - {self.plato.nombre_plato}'
    

class Factura(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Factura - {self.cliente.nombre} - {self.fecha_emision}'
    

class Pedido(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.proveedor.nombre_proveedor}"
    



