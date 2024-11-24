from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import UserAuth, UserRegistration, PasswordResetRequest
from .serializers import UserRegistrationSerializer, UserAuthSerializer, PasswordResetRequestSerializer

@api_view(['POST'])
def create_account(request):
    """Create a new user account."""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        # Save the user to UserAuth after password hashing
        user_registration = serializer.save()
        user_registration.save_user()
        return Response({"message": "Account created successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    """Authenticate user and login."""
    user_id = request.data.get('user_id')
    role = request.data.get('role')
    password = request.data.get('password')

    try:
        user_auth = UserAuth.objects.get(user_id=user_id, role=role)
        if user_auth.check_password(password):
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid password."}, status=status.HTTP_400_BAD_REQUEST)
    except UserAuth.DoesNotExist:
        return Response({"message": f"{role.capitalize()} with ID {user_id} not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def password_reset(request):
    """Reset user password."""
    serializer = PasswordResetRequestSerializer(data=request.data)
    if serializer.is_valid():
        reset_request = serializer.save()
        reset_request.reset_password()
        return Response({"message": "Password reset successfully."}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
