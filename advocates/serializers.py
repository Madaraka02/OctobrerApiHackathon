from rest_framework import serializers
from .models import *
from companies.serializers import *


class AdvocateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    company = CompanyUrlSerializer()
    class Meta:
        model = Profile
        fields = ['id','name','profile_pic','short_bio','long_bio','advocate_years_exp','company','links']




class AdvocatesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    class Meta:
        model = Profile
        fields = ['id','name','profile_pic','short_bio','long_bio','advocate_years_exp','links']        