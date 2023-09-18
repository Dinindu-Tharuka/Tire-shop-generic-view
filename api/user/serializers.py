from djoser.serializers import UserCreateSerializer
from djoser import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'user_name', 'email', 'password', 'is_manager', 'is_superuser']