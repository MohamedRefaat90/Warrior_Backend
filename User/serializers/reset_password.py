from rest_framework import serializers
from django.core.mail import send_mail
from ..models import PasswordOTP, Users
import random

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not Users.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user with this email.")
        return value

    def create_otp(self, user):
        otp = str(random.randint(100000, 999999))
        PasswordOTP.objects.create(user=user, otp=otp)
        return otp

    def send_otp_email(self, user, otp):
        send_mail(
            'Your Password Reset OTP',
            f'Use this OTP to reset your password: {otp}',
            'noreply@example.com',
            [user.email]
        )

    def save(self):
        email = self.validated_data['email']
        user = Users.objects.get(email=email)
        otp = self.create_otp(user)
        self.send_otp_email(user, otp)


class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = Users.objects.get(email=data['email'])
            otp_entry = PasswordOTP.objects.filter(user=user, otp=data['otp'], is_verified=False).latest('otp_created_at')
            if not otp_entry.is_otp_valid():
                raise serializers.ValidationError("OTP has expired.")
        except (Users.DoesNotExist, PasswordOTP.DoesNotExist):
            raise serializers.ValidationError("Invalid email or OTP.")

        self.otp_entry = otp_entry
        return data

    def save(self):
        # Mark OTP as verified
        self.otp_entry.is_verified = True
        self.otp_entry.save()
        
class PasswordConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)
    confirm_new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError("Passwords do not match.")

        try:
            user = Users.objects.get(email=data['email'])
            otp_entry = PasswordOTP.objects.filter(user=user, is_verified=True).latest('otp_created_at')
            if not otp_entry.is_otp_valid():
                raise serializers.ValidationError("OTP has expired or has not been verified.")
        except (Users.DoesNotExist, PasswordOTP.DoesNotExist):
            raise serializers.ValidationError("Invalid email or OTP verification.")

        self.user = user
        return data

    def save(self):
        new_password = self.validated_data['new_password']
        self.user.set_password(new_password)
        self.user.save()
        # Clean up OTPs after successful password reset
        PasswordOTP.objects.filter(user=self.user).delete()
