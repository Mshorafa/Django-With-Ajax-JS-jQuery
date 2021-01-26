from django.db import models

# Create your models here.

class DoTask(models.Model):
    title = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    completaed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering=['completaed','data']