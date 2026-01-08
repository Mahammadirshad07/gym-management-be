from rest_framework import serializers
from .models import GymUser

class GymUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymUser
        fields = '__all__' # Return all fields to the frontend

# Serializer specifically for updating weight (good practice to be specific)
class WeightUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymUser
        fields = ['weight']
