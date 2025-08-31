from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from .resources import CategoryResource, ProductResource

category_resource = CategoryResource()
product_resource = ProductResource()

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    list_per_page = 5
    resource_class = CategoryResource

@admin.register(Products)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name', 'cost',)
    list_editable = ('cost',)
    search_fields = ('name',)
    list_filter = ('category',)
    list_per_page = 5
    resource_class = ProductResource