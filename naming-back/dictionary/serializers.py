from rest_framework import serializers
from .models import *

class dictionarySerializer(serializers.ModelSerializer):
    firstName = serializers.SerializerMethodField()
    def get_firstName(self, obj):
        return obj.firstName

    class Meta:
        model = dictionary
        fields = ['id', 'userId', 'firstName', 'color', 'shadow', 'shadowColor', 'border']

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ['id', 'consonant', 'contents', 'likes']

class dictionaryPostSerializer(serializers.ModelSerializer):
    post = postSerializer(many = True, read_only = True)
    class Meta:
        model = dictionary
        fields = ['id', 'post']