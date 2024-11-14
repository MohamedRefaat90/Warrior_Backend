from rest_framework import serializers
from ..models import Users
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        user = authenticate(email = data['email'], password = data['password'])
        
        if user is None:
            raise serializers.ValidationError("Invalid Email or Password")
        if not user.is_active:
            raise serializers.ValidationError("User Account is Deactivated")
        
        data['user'] = user
        return data