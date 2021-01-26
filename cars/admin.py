from django.contrib import admin
from .models import Car


# Register your models here.
@admin.register(Car)
class carConfig(admin.ModelAdmin):
    list_display = ['name', 'country']
