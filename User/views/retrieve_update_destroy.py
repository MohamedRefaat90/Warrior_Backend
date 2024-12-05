from rest_framework import generics
from ..models import Users
from rest_framework.permissions import IsAuthenticated
from ..serializers.user import UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user