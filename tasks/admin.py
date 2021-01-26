from django.contrib import admin
from .models import DoTask

# Register your models here.

@admin.register(DoTask)
class CoutomDotoAdmin(admin.ModelAdmin):
    pass