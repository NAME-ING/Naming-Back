from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from dictionary.models import dictionary
from django.contrib.auth.hashers import make_password, check_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'firstName', 'password']

    def create(self, validate_data):
        hashed_password = make_password('password')
        user = User.objects.create(
            username=validate_data['username'],
            firstName=validate_data['firstName'],
            password=make_password(validate_data['password']),
        )
        # user.make_password(validate_data['password'])
        token = RefreshToken.for_user(user)
        user.refreshtoken = token
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            userId = user.objects.get(userId)
            if dictionary.objects.filter(userId=userId).exists():
                dictionaryId = dictionary.objects.get(userId=userId)
            else: 
                dictionaryId = ""
                
            if not user.check_password(password):
                raise serializers.ValidationError('잘못된 비밀번호입니다.')
            else:
                token = RefreshToken.for_user(user)
                refresh = str(token)
                access = str(token.access_token)

                data = {
                    'user_id' : user.id,
                    'username': user.username,
                    'firstName': user.firstName,
                    'access_token': access,
                    'dictionary': dictionaryId
                }

                return data
        else:
            raise serializers.ValidationError('존재하지 않는 사용자입니다.')
