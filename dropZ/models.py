from django.db import models


# Create your models here.

class DropZone(models.Model):
    file = models.ImageField(upload_to='dropZ/')

    def __str__(self):
        return f'{self.pk}'
