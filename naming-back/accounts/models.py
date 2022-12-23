from django.db import models

class accounts(models.Model):
    firstName = models.CharField(max_length=30, unique=False, null=False, default='')