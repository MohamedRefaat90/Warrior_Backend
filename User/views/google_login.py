import os
from django.contrib.auth.models import update_last_login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from google.oauth2 import id_token
from google.auth.transport import requests
from ..models import Users

@api_view(['POST'])
def google_sign_in(request):
    """
    Endpoint for Google Sign-In.
    """
    token = request.data.get('token')
    if not token:
        return Response({"error": "Token is required."}, status=400)

    try:
        # Verify the token
        userData = id_token.verify_oauth2_token(token, requests.Request(), os.environ.get('GOOGLE_CLIENT_ID'))
        
        # Extract user information
        email = userData.get('email')
        name = userData.get('name')
        picture = userData.get('picture')

        if not email:
            return Response({"error": "Email not provided in token."}, status=400)

        # Get or create user
        user, created = Users.objects.get_or_create(email=email)

        if not created:
            user.username = name
            # user.profile_picture = picture  # If you have a profile_picture field
            user.save()

        # Generate JWT token
        refresh = RefreshToken.for_user(user)

        # Update last login
        update_last_login(None, user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "email": email,
                "username": name,
                "profile_picture": user.profile_picture if hasattr(user, 'profile_picture') else None,
            },
        })
    except ValueError as e:
        return Response({f"error": e}, status=400)
