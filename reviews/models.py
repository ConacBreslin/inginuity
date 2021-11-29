from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from gins.models import Distillery


class Review(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    distillery = models.ForeignKey(Distillery, on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)
    first_created_on = models.DateTimeField(auto_now_add=True)
    last_editted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.distillery)

