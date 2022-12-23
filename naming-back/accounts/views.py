from .serializers import *
from .models import *
from rest_framework import views
from django.shortcuts import get_object_or_404
import uuid
from rest_framework.status import *
from rest_framework.response import Response

class accountsView(views.APIView):
    def post(self, request):
        serializer = RegisterForm(data=request.data)
        if serializer.is_valid():
            return Response({'data': serializer.data})