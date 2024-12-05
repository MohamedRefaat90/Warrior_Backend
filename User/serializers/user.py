from ..models import Users
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['id','email', 'username']
        read_only = ['id']
