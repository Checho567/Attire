from django.db import models
from inv.models import Products
from django.contrib.auth.models import AbstractUser

class Locality(models.Model):
    LOCALITY_CHOICES = (
        ('Usaquén', 'Usaquén'),
        ('Chapinero', 'Chapinero'),
        ('Santa Fe', 'Santa Fe'),
        ('San Cristóbal', 'San Cristóbal'),
        ('Usme', 'Usme'),
        ('Tunjuelito', 'Tunjuelito'),
        ('Bosa', 'Bosa'),
        ('Kennedy', 'Kennedy'),
        ('Fontibón', 'Fontibón'),
        ('Engativá', 'Engativá'),
        ('Suba', 'Suba'),
        ('Barrios Unidos', 'Barrios Unidos'),
        ('Teusaquillo', 'Teusaquillo'),
        ('Los Mártires', 'Los Mártires'),
        ('Antonio Nariño', 'Antonio Nariño'),
        ('Puente Aranda', 'Puente Aranda'),
        ('La candelaria', 'La candelaria'),
        ('Rafael Uribe Uribe', 'Rafael Uribe Uribe'),
        ('Ciudad Bolivar', 'Ciudad Bolivar'),
        ('Sumapaz', 'Sumapaz')
    )
    locality_names = models.CharField(max_length=18, choices=LOCALITY_CHOICES, help_text='Seleccione su localidad', verbose_name='Localidad', default='Usaquén')

    def __str__(self):
        return self.locality_names
    
    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        db_table = 'Localidad'
        ordering = ['id']

class Document(models.Model):
    TYPE_CHOICES = (
        ('CC', 'CC'),
        ('TI', 'TI'),
        ('CE', 'CE')
    )
    type_doc = models.CharField(max_length=2, choices=TYPE_CHOICES ,verbose_name='Tipo de documento')

    def __str__(self):
        return self.type_doc
    
    class Meta:
        verbose_name = 'TipoDocumento'
        verbose_name_plural = 'Tipo de documento'
        db_table = 'TipoDocumento'
        ordering = ['id']

class User(AbstractUser):
    address = models.CharField(max_length=50, verbose_name='Dirección', null=True, blank=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, verbose_name='Localidad', null=True, blank=True)
    zip_code = models.PositiveIntegerField(verbose_name='Código postal', null=True, blank=True)
    type_document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Tipo de documento', null=True, blank=True)
    number_document = models.BigIntegerField(verbose_name='Numero de documento', null=True)
    phone = models.BigIntegerField(verbose_name='Telefono', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios'
        ordering = ['id']



class method(models.Model):
    method = models.CharField(max_length=25, verbose_name='Metodo de pago')
    description = models.TextField(max_length=100, verbose_name='Descripción')

    def __str__(self):
        return self.method

    class Meta:
        verbose_name = 'Metodo de pago'
        verbose_name_plural = 'Metodos de pago'
        db_table = 'metodo_de_pago'
        ordering = ['id']