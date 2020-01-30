from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SiteFollowers(models.Model):
    tunnus = models.CharField(max_length=64)
    maili = models.EmailField()

    def __str__(self):
        return self.tunnus
