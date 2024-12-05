from rest_framework import generics
from ..models import Users
from ..serializers.create_user import CreateUserSerializer

class CreateUserView(generics.CreateAPIView):
    
    queryset = Users.objects.all()
    serializer_class = CreateUserSerializer
    