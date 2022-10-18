from rest_framework import serializers
from .models import *
from companies.models import *
from companies.serializers import *


class CompanyUrlSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='user.name')
    href = serializers.HyperlinkedIdentityField(
        view_name='company_details',
        lookup_field='id'
    )
    class Meta:
        model = CompanyProfile
        fields = ['id','name','logo','href']     
           



class AdvocateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    company = CompanyUrlSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['id','name','profile_pic','short_bio','long_bio','advocate_years_exp','company','links']        