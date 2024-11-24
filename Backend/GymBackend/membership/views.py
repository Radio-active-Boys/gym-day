from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MembershipType, Member, Attendance
from .serializers import MembershipTypeSerializer, MemberSerializer, AttendanceSerializer

# CRUD for MembershipType
class MembershipTypeList(APIView):
    def get(self, request):
        membership_types = MembershipType.objects.all()
        serializer = MembershipTypeSerializer(membership_types, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MembershipTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MembershipTypeDetail(APIView):
    def get(self, request, pk):
        try:
            # Assuming membership_type_id is the custom field
            membership_type = MembershipType.objects.get(membership_type_id=pk)
        except MembershipType.DoesNotExist:
            return Response({"error": "MembershipType not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MembershipTypeSerializer(membership_type)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            membership_type = MembershipType.objects.get(membership_type_id=pk)
        except MembershipType.DoesNotExist:
            return Response({"error": "MembershipType not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MembershipTypeSerializer(membership_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            membership_type = MembershipType.objects.get(membership_type_id=pk)
        except MembershipType.DoesNotExist:
            return Response({"error": "MembershipType not found"}, status=status.HTTP_404_NOT_FOUND)
        membership_type.delete()
        return Response({"message": "MembershipType deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# CRUD for Member
class MemberList(APIView):
    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MemberDetail(APIView):
    def get(self, request, pk):
        try:
            # Assuming member_id is the custom field
            member = Member.objects.get(member_id=pk)
        except Member.DoesNotExist:
            return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            member = Member.objects.get(member_id=pk)
        except Member.DoesNotExist:
            return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            member = Member.objects.get(member_id=pk)
        except Member.DoesNotExist:
            return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)
        member.delete()
        return Response({"message": "Member deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# CRUD for Attendance
class AttendanceList(APIView):
    def get(self, request):
        attendances = Attendance.objects.all()
        serializer = AttendanceSerializer(attendances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttendanceDetail(APIView):
    def get(self, request, pk):
        try:
            # Assuming attendance_id is the custom field
            attendance = Attendance.objects.get(attendance_id=pk)
        except Attendance.DoesNotExist:
            return Response({"error": "Attendance not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            attendance = Attendance.objects.get(attendance_id=pk)
        except Attendance.DoesNotExist:
            return Response({"error": "Attendance not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            attendance = Attendance.objects.get(attendance_id=pk)
        except Attendance.DoesNotExist:
            return Response({"error": "Attendance not found"}, status=status.HTTP_404_NOT_FOUND)
        attendance.delete()
        return Response({"message": "Attendance deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
