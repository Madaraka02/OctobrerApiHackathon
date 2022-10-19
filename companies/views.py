from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from advocates.paginations import CustomPagination
from rest_framework import filters

class CompanyList(generics.ListCreateAPIView):
    search_fields = ['user__name']
    filter_backends = (filters.SearchFilter,)
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanySerializer
    pagination_class = CustomPagination



class CompanyDetail(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyDetailsSerializer
 
class CompanyUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanySerializer       

class CompanyDestroyView(generics.DestroyAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyDetailsSerializer     