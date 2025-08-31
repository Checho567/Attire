from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='Nombre')
    description = models.TextField(max_length=100, verbose_name='Descripción')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']

class Products(models.Model):
    name = models.CharField(max_length=40, verbose_name='Nombre')
    size = models.CharField(max_length=3, verbose_name='Talla')
    cost = models.FloatField(max_length=20, verbose_name='Valor')
    photo = models.ImageField(upload_to='static/photo/%Y/%m/%d', null=True, blank=True, verbose_name='Foto')
    amount = models.IntegerField(verbose_name='Cantidad')
    PUBLIC_CHOICES = [
        ('Hombres', 'Hombres'),
        ('Mujeres', 'Mujeres'),
        ('Niños', 'Niños'),
    ]
    public = models.CharField(max_length=10, choices=PUBLIC_CHOICES, help_text='Seleccione el publico preferido', verbose_name='Publico preferido')
    category = models.ManyToManyField(Category)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']
