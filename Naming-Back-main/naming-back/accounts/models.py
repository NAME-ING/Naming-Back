from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    loginId = models.CharField(
        max_length=30, unique=True, null=False, default='')
    firstName = models.CharField(
        max_length=20, null=False, unique=False, default='')
