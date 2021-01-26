from django.contrib import admin
from .models import DropZone


# Register your models here.
@admin.register(DropZone)
class coustomDropZone(admin.ModelAdmin):
    pass
