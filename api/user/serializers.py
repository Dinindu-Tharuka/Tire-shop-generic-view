from djoser.serializers import UserCreateSerializer
from djoser import serializers
from rest_framework import serializers as base_serializer
from django.contrib.auth import get_user_model
from user_data.models import UserProfile, UserAccount
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'user_name', 'email', 'password', 'is_manager']

class UserProfileSerializer(base_serializer.ModelSerializer):
    user_account_id = base_serializer.IntegerField(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'user_account_id']

class UserProfileCreateSerializer(base_serializer.ModelSerializer):
    user_account_id = base_serializer.IntegerField()
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'user_account_id']

    

class UserSerializer(base_serializer.ModelSerializer):
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'user_name', 'email', 'password', 'is_manager', 'profile']

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = UserAccount.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user_account_id=user.id, **profile)
        return user
    
   