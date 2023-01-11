from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    firstName = models.CharField(
        max_length=20, unique=False, null=False)
    loginId = models.CharField(
        max_length=30, unique=True, null=False, default='')
