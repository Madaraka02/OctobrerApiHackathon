from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics


class AdvocateList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = AdvocatesSerializer


class AdvocateDetail(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Profile.objects.all()
    serializer_class = AdvocateSerializer
 
class AdvocateUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Profile.objects.all()
    serializer_class = AdvocateSerializer       

class AdvocateDestroyView(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = AdvocateSerializer    
