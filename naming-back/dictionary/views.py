from .serializers import *
from .models import *
from rest_framework import views
from django.shortcuts import get_object_or_404
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class dictionaryView(views.APIView):
    def get(self, request, pk, format=None):
        dictionarymake = get_object_or_404(dictionary, pk=pk)
        self.check_object_permissions(self.request, dictionarymake)
        serializer = dictionarySerializer(dictionarymake)
        return Response({'message':'사전 보여주기 성공', 'data':serializer.data}, status=HTTP_200_OK)

class dictionaryMakeView(views.APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = dictionarySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'사전 만들기 성공', 'data': serializer.data}, status=HTTP_201_CREATED)
        return Response({'message': '사전 만들기 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

class postListView(views.APIView):
    serializer_class = postSerializer

    def get_object(self, pk, format=None):
        postget = get_object_or_404(dictionary, pk=pk)
        return postget
    
    def get(self, request, pk):
        consonant = request.GET.get('consonant')
        params = {'consonant': consonant}
        arguments = {}
        for key, value in params.items():
            if value:
                arguments[key] = value

        postall = get_object_or_404(dictionary, pk=pk)
        
        postfilter = post.objects.filter(**arguments, dictionary=postall)

        serializer = self.serializer_class(postfilter, many=True)
        return Response({'message':'정의 보여주기 성공', 'data': serializer.data}, status=HTTP_200_OK)
    
    def post(self, request, pk):
        postmake = get_object_or_404(dictionary, pk=pk)
        serializer = postSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(dictionary = postmake)
            return Response({'message':'정의 적기 성공', 'data': serializer.data},status=HTTP_200_OK)
        return Response({'message': '정의 적기 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

class postDeleteView(views.APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk, format=None):
        postit = get_object_or_404(post, pk=pk)
        self.check_object_permissions(self.request, postit)
        return postit

    def delete(self, request, pk, post_pk):
        post = self.get_object(pk = post_pk)
        post.delete()
        return Response({'message':'정의 삭제 성공'}, status=HTTP_200_OK)