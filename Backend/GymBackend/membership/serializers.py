from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import MembershipType, Member, Attendance

class MembershipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipType
        fields = '__all__'  # Include all fields or specify explicitly

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

    def validate(self, data):
        if data['check_out_time'] <= data['check_in_time']:
            raise ValidationError("Check-out time must be after check-in time.")
        return data
