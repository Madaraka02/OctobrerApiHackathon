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
    # name = serializers.PrimaryKeyRelatedField(queryset = get_user_model().objects.filter(is_company=True) ,source = 'user.name',)
    class Meta:
        model = CompanyProfile
        fields = ['id','name','logo','summary']   



    def update(self, instance, validated_data):
        profile_data = validated_data.pop('user')

        user = instance.user

        instance.logo = validated_data.get(
            'logo', instance.logo)
        instance.summary = validated_data.get(
            'summary', instance.summary)
        instance.save()


       
        user.email = profile_data.get(
            'email', user.email)
        user.name = profile_data.get(
            'name', user.name)
        user.is_company=True    
        user.save()

        return instance             


             