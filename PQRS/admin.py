from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(type)
admin.site.register(Status)


@admin.register(Pqrs)
class PqrsAdmin(ImportExportModelAdmin):
    list_display = ('client', 'type', 'status', 'description', 'answer')
    list_editable = ('status', 'answer')
    list_per_page = 1
