from rest_framework import serializers
from .models import *

class dictionaryMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = dictionary
        fields = ['id', 'userId', 'firstName', 'color', 'shadow', 'shadowColor', 'border']

class dictionarySerializer(serializers.ModelSerializer):
    stacked = serializers.IntegerField(default=0, read_only = True)
    class Meta:
        model = dictionary
        fields = ['id', 'userId', 'firstName', 'color', 'shadow', 'shadowColor', 'border', 'stacked']

class postSerializer(serializers.ModelSerializer):
    is_liked = serializers.BooleanField(default=False)
    likes = serializers.IntegerField(default=0, read_only = True)

    class Meta:
        model = post
        fields = ['id', 'consonant', 'contents', 'likes', 'is_liked']

class dictionaryListSerializer(serializers.ModelSerializer):
    stacked = serializers.IntegerField(default=0, read_only = True)
    firstName = serializers.SerializerMethodField()
    def get_firstName(self, obj):
        return obj.firstName

    class Meta:
        model = dictionary
        fields = ['id', 'userId', 'firstName', 'color', 'shadow', 'shadowColor', 'border', 'stacked']

class dictionaryPostSerializer(serializers.ModelSerializer):
    post = postSerializer(many = True, read_only = True)
    class Meta:
        model = dictionary
        fields = ['id', 'post']

class NickNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = post
        fields = ['id', 'nickname']

class dictionaryFindSerializer(serializers.ModelSerializer):
    class Meta:
        model = dictionary
        fields = ['id']