from email import message
import imp
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import HelloSerializer
from rest_framework import serializers
from rest_framework import status

# Create your views here.

class HelloViewSet(viewsets.ViewSet):
    serializer_class = HelloSerializer
    
    def list(self,request):
        list = ['test1','test2','test3']
        return Response({'message':'Helloo','list':list})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name }!'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        return Response(({'http_method':'GET'}))

    def update(self,request,pk=None):
        return Response(({'http_method':'PUT'}))

    def partial_update(self,request,pk=None):
        return Response(({'http_method':'PATCH'}))

    def destroy(self,request,pk=None):
        return Response(({'http_method':'DELETE'}))