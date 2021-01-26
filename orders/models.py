from django.db import models


# Create your models here.


class Order(models.Model):
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE)
    model = models.ForeignKey('models.Model', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}'
