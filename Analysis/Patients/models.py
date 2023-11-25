from django.db import models

# Create your models here.

class Technicians(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return self.name