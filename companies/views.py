from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics


class CompanyList(generics.ListCreateAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyDetailsSerializer
 
class CompanyUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyDetailsSerializer       

class CompanyDestroyView(generics.DestroyAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyDetailsSerializer     