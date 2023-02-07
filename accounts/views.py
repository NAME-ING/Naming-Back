
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework.status import *
from rest_framework import views
from rest_framework.response import Response

import jwt
import datetime
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import views
from rest_framework.status import *
from rest_framework.response import Response


from .models import *
from .serializers import *


class SignUpView(views.APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            firstName = serializer.validated_data['firstName']
            users = User.objects.filter(firstName=firstName)
            number = len(users)
            serializer.save(userNumber=number)
            return Response({'message': '회원가입 성공', 'data': serializer.data}, status=HTTP_201_CREATED)
        return Response({'message': '회원가입 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'message': "로그인 성공", 'data': serializer.validated_data}, status=HTTP_200_OK)
        return Response({'message': "로그인 실패", 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)


class UserNumberView(views.APIView):
    serializer_class = UserSerializer
    def get(self, request, pk):
        UserNumber = User.objects.get(id = pk)
        serializer = self.serializer_class(UserNumber)
        return Response({'message': '몇번째 유저 찾기 성공', 'data': serializer.data}, status = HTTP_200_OK)