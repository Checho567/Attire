from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Category, Products
from import_export.formats.base_formats import XLSX


class CategoryResource(resources.ModelResource):
    custom_name = fields.Field(
        attribute='name', column_name='Categoria')
    custom_description = fields.Field(
        attribute='description', column_name='Descripción')

    class Meta:
        model = Category
        fields = ('custom_name', 'custom_description')
        export_order = ('custom_name', 'custom_description')
        formats = ['xlsx']

class ProductResource(resources.ModelResource):
    custom_name = fields.Field(attribute='name', column_name='Producto')
    custom_cost = fields.Field(attribute='cost', column_name='Valor')
    custom_amount = fields.Field(attribute='amount', column_name='Cantidad')

    class Meta:
        model = Products
        fields = ('custom_name', 'custom_cost', 'custom_amount')
        export_order = ('custom_name', 'custom_cost', 'custom_amount')
        formats = ['xlsx']
