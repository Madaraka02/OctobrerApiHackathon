from rest_framework import serializers
from .models import *


class CompanyDetailsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    advocates = serializers.StringRelatedField(many=True)
    class Meta:
        model = CompanyProfile
        fields = ['id','name','logo','summary','advocates']

class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    class Meta:
        model = CompanyProfile
        fields = ['id','name','logo','summary']        