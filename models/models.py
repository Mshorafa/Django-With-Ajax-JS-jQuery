from django.db import models
# Create your models here.


class Model(models.Model):
    name = models.CharField(max_length=50)
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


