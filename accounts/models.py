from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    firstName = models.CharField(max_length=100, null=False, blank=False)

    USERNAME_FIELD = 'username'