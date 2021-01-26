from django.db import models


# Create your models here.


class CroopImag(models.Model):
    file = models.ImageField(upload_to='images')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}'
