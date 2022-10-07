from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics


class CompanyList(generics.ListCreateAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanySerializer