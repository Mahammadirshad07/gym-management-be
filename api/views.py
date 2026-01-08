from django.contrib.auth import authenticate  # <--- IMPORT THIS
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import GymUser
from .serializers import GymUserSerializer, WeightUpdateSerializer
from django.shortcuts import get_object_or_404


# ================= ADMIN ENDPOINTS =================

@api_view(['POST'])
def admin_login(request):
    """
    Endpoint: /admin-login/
    Expects: {"username": "admin", "password": "password123"}
    """
    username = request.data.get('username')
    password = request.data.get('password')

    # This checks against the Superuser you created with 'createsuperuser'
    user = authenticate(username=username, password=password)

    if user is not None and user.is_superuser:
        return Response({"message": "Login successful", "admin": True}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def create_user(request):
    """
    Endpoint: /admin/create-user
    Expects JSON: All user fields
    """
    serializer = GymUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_all_users(request):
    """
    Endpoint: /admin/viewdetails
    Returns: List of all users
    """
    users = GymUser.objects.all()
    serializer = GymUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_user_admin(request, pk):
    """
    Endpoint: /admin/update-user/<id>
    Used by admin to update subscription or other details
    """
    user = get_object_or_404(GymUser, pk=pk)
    # partial=True allows updating just one field (like subscription) without sending all data
    serializer = GymUserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ================= USER ENDPOINTS =================


@api_view(['POST'])
def user_login_via_mobile(request):
    """
    Endpoint: /users/login
    Expects: {"mobile_number": "1234567890"}
    Returns: User details if found
    """
    mobile = request.data.get('mobile_number')
    if not mobile:
        return Response({"error": "Mobile number required"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Try to find user
    try:
        user = GymUser.objects.get(mobile_number=mobile)
        serializer = GymUserSerializer(user)
        return Response(serializer.data)
    except GymUser.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_user_detail(request, pk):
    """
    Endpoint: /users/<id>
    Get specific user details
    """
    user = get_object_or_404(GymUser, pk=pk)
    serializer = GymUserSerializer(user)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_weight(request, pk):
    """
    Endpoint: /users/update-weight/<id>
    Used by user to update only their weight
    """
    user = get_object_or_404(GymUser, pk=pk)
    serializer = WeightUpdateSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, pk):
    user = get_object_or_404(GymUser, pk=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

