from .models import Technicians
from django.contrib.auth.models import User
from rest_framework import serializers


class TechnicainSerializer(serializers.ModelSerializer):
    class Meta:
        model=Technicians
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
'''
class TechnicainSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    gender = serializers.CharField(max_length=50)
    age=serializers.IntegerField()

    def create(self, validated_data):
        return Technicians.objects.create(**validated_data)

    def update(self, technicnian, validated_data):
        newTechninan=Technicians(**validated_data)
        newTechninan.id=technicnian.id
        newTechninan.save()
        return new
'''
class UserSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()
