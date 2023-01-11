from django.contrib.auth.forms import UserCreationForm
from .models import *
from rest_framework import serializers


class RegisterForm(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'loginId', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            userid=validated_data['loginId'],)
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        loginId = data.get("loginId", None)
        password = data.get("password", None)

        if User.objects.filter(loginId=loginId).exists():
            user = User.objects.get(loginId=loginId)

            if not user.check_password(password):
                raise serializers.ValidationError()
            else:
                return user
        else:
            raise serializers.ValidationError()
