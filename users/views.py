from django.shortcuts import render
from .serializers import *
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

# Create your views here.
class CompanyRegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(is_company = True)
            response = {
                "message":"Created succcessfully",
                "data":serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class AdvocateRegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(is_advocate = True)
            response = {
                "message":"Created succcessfully",
                "data":serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
