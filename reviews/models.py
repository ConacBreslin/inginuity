from django.db import models

# Create your models here.
class Review(models.Model):
   
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True, blank=True)
    body = models.CharField(max_length=10)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title