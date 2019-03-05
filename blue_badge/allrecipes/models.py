from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=40)
    ingredients = models.CharField(max_length=500)
    instructions = models.CharField(max_length=2000)

    def __str__(self):
        return self.name