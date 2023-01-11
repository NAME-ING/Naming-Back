from .serializers import *
from .models import *
from rest_framework import views
from django.shortcuts import get_object_or_404
import uuid
from rest_framework.status import *
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.permissions import IsAuthenticated


class RegistrationView(views.APIView):
    serializer_class = RegisterForm

    def post(self, request):
        serializer = RegisterForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response({'error': serializer.errors})  # 피그마 보고 수정하기
