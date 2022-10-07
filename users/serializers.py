from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=10, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name','password']


    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        
        if email_exists:
            raise ValidationError('Email is already taken')
            
        return super().validate(attrs)

    def create(self, validated_data):

        password = validated_data.pop("password")
        user = super().create(validated_data)  
        user.set_password(password)
        user.save()

        return  user