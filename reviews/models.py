from django.db import models
from django.contrib.auth.models import User
from gins.models import Distillery
from profiles.models import UserProfile


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    distillery = models.ForeignKey(Distillery, on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)
    first_created_on = models.DateTimeField(auto_now_add=True)
    last_editted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.distillery)
