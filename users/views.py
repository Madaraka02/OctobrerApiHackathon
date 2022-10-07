from django.shortcuts import render
from .serializers import *
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

# Create your views here.
class CompanyRegisterView(generics.GenericAPIView):
    serializer_class = CompanyRegisterSerializer

    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            usser = serializer.save(commit=False)
            usser.is_company = True
            usser.save()

            response = {
                "message":"Created succcessfully",
                "data":serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    



