from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, user_name, email, password=None, **other_fields):
        if not email:
            return ValueError('Email field must be required.')
        
        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(user_name=user_name, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, user_name, email, password=None, **other_fields):
        user = self.create_user(user_name, email, password, **other_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

class UserAccount(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'is_manager', 'is_superuser']

class UserProfile(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


