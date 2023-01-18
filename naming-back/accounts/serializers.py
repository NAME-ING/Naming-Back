from django.contrib.auth.forms import UserCreationForm
from rest_framework import serializers
from .models import accounts

class RegisterForm(UserCreationForm):
    class Mete:
        model = accounts
        fields = ['email']