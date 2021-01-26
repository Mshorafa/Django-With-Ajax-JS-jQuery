from django.contrib import admin
from .models import CroopImag


# Register your models here.
@admin.register(CroopImag)
class CroopImagCoustom(admin.ModelAdmin):
    list_display = ['pk', 'file', 'uploaded']
