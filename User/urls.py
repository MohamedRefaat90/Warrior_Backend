from django.urls import path
from .views.reset_password import *
from .views.create_user import CreateUserView
from .views.email_login import LoginView
from .views.retrieve_update_destroy import UserRetrieveUpdateDestroyView
from .views.reset_password import PasswordResetRequestView, PasswordResetOTPVerificationView
from .views.google_login import google_sign_in
urlpatterns = [
    path('Signup/', CreateUserView.as_view(), name="Signup"),
    path('Login/', LoginView.as_view(), name="Login"),
    path('User/', UserRetrieveUpdateDestroyView.as_view(), name="getUser"),
    path('forget-password/', PasswordResetRequestView.as_view(), name='forget-password'),
    path('otp-verification/', PasswordResetOTPVerificationView.as_view(), name='otp-verification'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('google-login/', google_sign_in, name='google-login'),
]
