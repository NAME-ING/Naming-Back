from django.contrib.auth.forms import UserCreationForm
from .models import *
from rest_framework import serializers


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['id', 'userid', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            userid=validated_data['userid'],)
        user.set_password(validated_data['password'])
        user.save()

        return user
