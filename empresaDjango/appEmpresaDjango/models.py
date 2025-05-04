from django.db import models
import datetime

class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.id} -> {self.dni}'

class Tarea(models.Model):
    PRIORIDAD_CHOICES = [
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    ]

    ESTADO_CHOICES = [
        ('Abierta', 'Abierta'),
        ('Asignada', 'Asignada'),
        ('En proceso', 'En proceso'),
        ('Finalizada', 'Finalizada'),
    ]

    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=1000)
    inicio = models.DateField(default=datetime.date.today)
    fin = models.DateField(default=datetime.date.today)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='Media')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Abierta')
    notas = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.id} -> {self.nombre}'

class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=1000)
    inicio = models.DateField(default=datetime.date.today)
    fin = models.DateField(default=datetime.date.today)
    presupuesto = models.CharField(max_length=150)
    cliente = models.CharField(max_length=150)
    tareas = models.ManyToManyField(Tarea)
    empleados = models.ManyToManyField(Empleado)

    def __str__(self):
        return f'{self.id} -> {self.nombre}'
