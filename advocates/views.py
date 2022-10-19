from django.shortcuts import render
from .models import *
from .serializers import *
from companies.serializers import *
from rest_framework import generics
from rest_framework import filters
from .paginations import CustomPagination


class AdvocateList(generics.ListCreateAPIView):
    search_fields = ['user__name']
    filter_backends = (filters.SearchFilter,)
    queryset = Profile.objects.all()
    serializer_class = AdvocatesSerializer
    pagination_class = CustomPagination
    


class AdvocateDetail(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Profile.objects.all()
    serializer_class = AdvocateSerializer
 
class AdvocateUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Profile.objects.all()
    serializer_class = AdvocateEditSerializer       

class AdvocateDestroyView(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = AdvocateSerializer    
