from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_superuser(self, userId, firstName=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(userId, firstName, email, password, **extra_fields)

    def create_user(self, userId, firstName, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        email = self.normalize_email(email)

        userId = self.model(userId)
        firstName = self.model(firstName)
        password = userId.set_password(password)
        userId.save()
        return firstName


class User(AbstractUser):
    username = None
    userId = models.CharField(
        unique=True, max_length=30, default='')
    firstName = models.CharField(
        unique=False, null=False, max_length=30, default='')
    email = models.EmailField(unique=True, max_length=100)

    USERNAME_FIELD = 'userId'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.userId
