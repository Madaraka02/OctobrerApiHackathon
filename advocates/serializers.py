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
           


class AdvocateEditSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    company = serializers.PrimaryKeyRelatedField(queryset = CompanyProfile.objects.filter())
    # company = CompanyUrlSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['id','name','profile_pic','short_bio','long_bio','advocate_years_exp','youtube','twitter','github','company']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('user')
        user = instance.user

        instance.profile_pic = validated_data.get(
            'profile_pic', instance.profile_pic)
        instance.short_bio = validated_data.get(
            'short_bio', instance.short_bio)
        instance.long_bio = validated_data.get(
            'long_bio', instance.long_bio)
        
        instance.advocate_years_exp = validated_data.get(
            'advocate_years_exp', instance.advocate_years_exp)
        instance.company = validated_data.get(
            'company', instance.company)
        instance.youtube = validated_data.get(
            'youtube', instance.youtube)
        instance.twitter = validated_data.get(
            'twitter', instance.twitter)
        instance.github = validated_data.get(
            'github', instance.github)

        instance.save()


       
        user.email = profile_data.get(
            'email', user.email)
        user.name = profile_data.get(
            'name', user.name)
        user.is_advocate=True    
        user.save()

        return instance

        

class AdvocateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    company = CompanyUrlSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['id','name','profile_pic','short_bio','long_bio','advocate_years_exp','company','links']        