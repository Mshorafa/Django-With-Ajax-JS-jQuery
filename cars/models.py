from django.db import models


# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
