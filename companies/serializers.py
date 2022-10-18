from rest_framework import serializers
from .models import *
from advocates.models import *



class AdvocatesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    class Meta:
        model = Profile
        fields = ['id','name','profile_pic','short_bio','long_bio','advocate_years_exp','links']  

class CompanyDetailsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    advocates = AdvocatesSerializer(many=True)
    class Meta:
        model = CompanyProfile
        fields = ['id','name','logo','summary','advocates']

class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    class Meta:
        model = CompanyProfile
        fields = ['id','name','logo','summary']        


             