from django.db import models


# Create your models here.
class Distillery(models.Model):

    class Meta:
        verbose_name_plural = 'Distilleries'

    name = models.CharField(max_length=100)
    town = models.CharField(max_length=50, null=True, blank=True)
    county = models.CharField(max_length=10)
    province = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    hasvisitorcentre = models.BooleanField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Gin(models.Model):
    name = models.CharField(max_length=254)
    distillery = models.ForeignKey(
        'Distillery', null=True, blank=True, on_delete=models.SET_NULL
        )
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
