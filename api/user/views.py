from django.shortcuts import render
from user_data.models import UserAccount
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveDestroyAPIView, ListAPIView
from .serializers import UserCreateSerializer
from api.paginations import DefaultPagination
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# class UserCreateView(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             user_name = data['user_name']
#             email = data['email']
#             email = email.lower()
#             password = data['password']
#             re_password = data['re_password']
#             is_manager = data['is_manager']

#             if password == re_password:
#                 if not UserAccount.objects.filter(email==email).exists():
#                     UserAccount.objects.create(user_name=user_name, email=email, password=password, is_manager=is_manager)
#                     return Response({'User created successfully.'}, status=status.HTTP_201_CREATED)
#                 else:
#                     return Response('Email is already exists.', status=status.HTTP_400_BAD_REQUEST)
                
#             else:
#                 return Response('Password do not match with Confirmation password.', status=status.HTTP_400_BAD_REQUEST)

#         except:
#             return Response('Sothing went wrong with adding user.', status=status.HTTP_400_BAD_REQUEST)
            


class UserView(ListAPIView):    
    queryset = UserAccount.objects.all()
    serializer_class = UserCreateSerializer
    

class UserDetailView(RetrieveDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserCreateSerializer