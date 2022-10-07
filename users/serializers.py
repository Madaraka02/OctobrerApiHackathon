from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=10, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name','password']


    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        
        if email_exists:
            raise ValidationError('Email is already taken')
            
        return super().validate(attrs)