from django.db import models
from datetime import datetime
from pedido.models import User

class type(models.Model):
    TYPE_CHOICES = (
        ('Petición', 'Petición'),
        ('Queja', 'Queja'),
        ('Reclamo', 'Reclamo'),
        ('Sugerencia', 'Sugerencia')
    )

    type_pqrs = models.CharField(max_length=10, choices=TYPE_CHOICES, help_text='Seleccione su tipo de QPRS', verbose_name='Tipo de pqrs', default='Petición')

    def __str__(self):
        return self.type_pqrs

    class Meta:
        verbose_name = 'Tipo_pqrs'
        verbose_name_plural = 'Tipos_pqrs'
        db_table = 'tipo'
        ordering = ['id']

class Status(models.Model):
    STATUS_CHOICES = (
        ('En trámite', 'En trámite'),
        ('Aceptada','Aceptada'),
        ('Rechazada', 'Rechazada')
    )
    status = models.CharField(max_length=10, verbose_name='Estado actual', choices=STATUS_CHOICES, default='En trámite')
    
    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        db_table = 'estado_pqrs'
        ordering = ['id']
        
class Pqrs(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Cliente')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de reporte')
    type = models.ForeignKey(type, on_delete=models.CASCADE, verbose_name='Tipo de PQRS')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Estado actual', null=True)
    description = models.TextField(max_length=500, verbose_name='Descripción')
    answer = models.TextField(max_length=500, verbose_name='Respuesta', null=True)
    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'pqrs'
        verbose_name_plural = 'pqrs'
        db_table = 'pqrs'
        ordering = ['id']

