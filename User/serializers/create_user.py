from ..models import Users
from rest_framework import serializers
from django.core.validators import validate_email
class CreateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    
    def validate_email(self, value):
        if validate_email(value):
            raise serializers.ValidationError("Please enter a valid email")
        
        elif Users.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        
        return value
    
    def create(self , validated_data):
        password = validated_data.pop('password')
        user = Users(**validated_data)
        user.set_password(password)
        user.save()
        return user
        
