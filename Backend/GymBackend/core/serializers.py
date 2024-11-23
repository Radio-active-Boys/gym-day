from rest_framework import serializers
from .models import Admin, Equipment, Maintenance

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'  # Include all fields or specify explicitly

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    equipment_name = serializers.ReadOnlyField(source='equipment.name')  # For displaying equipment name

    class Meta:
        model = Maintenance
        fields = '__all__'
