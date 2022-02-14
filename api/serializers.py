# This file converts model instances to JSON for the frontend
from rest_framework import serializers
from .models import Vase, Plate

# Vase Serializer 
class VaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vase
        fields = '__all__'

# Plate Serializer
class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = '__all__'
