from rest_framework.permissions import AllowAny
from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response
from ..serializers.login import LoginSerializer
from ..models import Users
from django.dispatch import receiver

class LoginView(KnoxLoginView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny] 
    
    def post(self,request ,*args, **kwargs):
        
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        
        self.request.user = user
        login_response = super(LoginView, self).post(request, format=None)
        token = login_response.data['token']
        
        return Response({
            'user': {
                "id": user.id,
                'username': user.username,
                'email': user.email
                },
            'token': token
        })

