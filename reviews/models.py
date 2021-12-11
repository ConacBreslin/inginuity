"""The Review model"""
from django.db import models
from django.contrib.auth.models import User
from gins.models import Distillery


class Review(models.Model):
    """Model for reviews"""
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 null=True, blank=True)
    distillery = models.ForeignKey(Distillery, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.CharField(max_length=1000)
    firstcreated = models.DateTimeField(auto_now_add=True)
    lasteditted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.distillery)
