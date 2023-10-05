from django.shortcuts import render
from user_data.models import UserAccount, UserProfile
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from .serializers import UserSerializer, UserProfileSerializer


class UserView(ListCreateAPIView):    
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer
    

class UserDetailView(RetrieveDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer

class UserProfileListView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetailView(RetrieveDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer