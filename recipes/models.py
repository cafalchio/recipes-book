from django.db import models
from PIL import Image

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=50 )
    description = models.TextField()
    cooking_time = models.CharField(max_length=50)
    servings = models.SmallIntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()
    servings = models.CharField(max_length=50)
    image = models.URLField(max_length=200, blank=True, null=True)
    is_public = models.BooleanField(default=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # code from https://stackoverflow.com/questions/24373341/django-image-resizing-and-convert-before-upload
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    