from django.contrib import admin
from .models import Model


# Register your models here.

@admin.register(Model)
class modelConfig(admin.ModelAdmin):
    list_display = ['name', 'car']
