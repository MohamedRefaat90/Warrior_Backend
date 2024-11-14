from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
from django.core.validators import validate_email
from rest_framework import serializers
from django.utils.translation import gettext as _
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class CustomUserManager(BaseUserManager):
    
    def create(self, email, password= None, **extra):
        try:
            validate_email(email)
        except:
            raise serializers.ValidationError({"email":_("Please enter a valid email")})
        
        email = self.normalize_email(email).lower()
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create(
            email,
            password,
            **extra_fields,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class Users(AbstractUser):
    
    class Meta:
        db_table = "Users"
    
    id = models.UUIDField(primary_key= True, default= uuid.uuid4)
    email = models.EmailField(max_length=225, unique=True)
    username = models.CharField(max_length=50, blank=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    
    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        super().save(*args, **kwargs)
    
            

class PasswordOTP(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='otp')
    otp = models.CharField(max_length=6)  
    otp_created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    def is_otp_valid(self):
        
        expiration_time = self.otp_created_at + timedelta(minutes=1)
        return timezone.now() < expiration_time

