from rest_framework import serializers
from .models import Request_Image_Model, Initiate_AI_Model

class InitiateAI_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Initiate_AI_Model
        fields = ['name']

class Image_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Request_Image_Model
        fields = ['image']
        