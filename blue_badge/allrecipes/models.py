from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=40)
    ingredients = models.CharField(max_length=500)
    instructions = models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.BooleanField(default=False)
    image = models.ImageField(default='default.gif', upload_to='profile_pics')

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        super().save(**kwargs)

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)