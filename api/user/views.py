from django.shortcuts import render
from user_data.models import UserAccount, UserProfile
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import UserSerializer, UserProfileSerializer, UserProfileCreateSerializer


class UserView(ListCreateAPIView):    

    def get_queryset(self):      
        if self.request.user.is_superuser:
            queryset = UserAccount.objects.all()
        elif self.request.user.is_manager:
            queryset_1 = UserAccount.objects.filter(is_staff=False).filter(is_manager=False)
            queryset_2 = UserAccount.objects.filter(id = self.request.user.id)
            queryset = queryset_1.union(queryset_2)
        else:
            queryset = UserAccount.objects.filter(id = self.request.user.id)        
        return queryset
    serializer_class = UserSerializer

    
    

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer

class UserProfileListView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileCreateSerializer   
        

class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

