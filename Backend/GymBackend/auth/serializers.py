from rest_framework import serializers
from .models import UserAuth, UserRegistration, PasswordResetRequest

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['user_id', 'role', 'password']

    def validate(self, data):
        if not UserRegistration.check_user_exists(data['user_id'], data['role']):
            raise serializers.ValidationError(f"{data['role']} with ID {data['user_id']} does not exist.")
        return data


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ['user_id', 'role', 'hashed_password']

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long.")
        return value


class PasswordResetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordResetRequest
        fields = ['user_id', 'role', 'new_password']

    def validate(self, data):
        if not UserRegistration.check_user_exists(data['user_id'], data['role']):
            raise serializers.ValidationError(f"{data['role']} with ID {data['user_id']} does not exist.")
        return data
