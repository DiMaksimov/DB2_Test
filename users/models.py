from django.contrib.auth.models import AbstractUser
from django.db import models


class DB2User(AbstractUser):
    birthday = models.DateField(null=True)
    country = models.CharField(max_length=50, default='Unknown')
    city = models.CharField(max_length=50, default='Unknown')

    def __str__(self):
        return self.email
