from email import message
import imp
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import HelloSerializer, ProfileFeedItemSerializer,UserProfileSerializer
from rest_framework import serializers
from rest_framework import status
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

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


class UserProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
    serializer_class = UserProfileSerializer
    queryset =models.UserProfile.objects.all()


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus,IsAuthenticated,)

    def perform_create(self,serializer):
        serializer.save(user_profile = self.request.user)