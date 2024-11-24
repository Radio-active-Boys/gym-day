from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Admin, Equipment, Maintenance
from .serializers import AdminSerializer, EquipmentSerializer, MaintenanceSerializer

# Admin CRUD
class AdminList(APIView):
    def get(self, request):
        admins = Admin.objects.all()
        serializer = AdminSerializer(admins, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminDetail(APIView):
    def get(self, request, pk):
        try:
            admin = Admin.objects.get(admin_id=pk)
        except Admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AdminSerializer(admin)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            admin = Admin.objects.get(admin_id=pk)
        except Admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AdminSerializer(admin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            admin = Admin.objects.get(admin_id=pk)
        except Admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)
        admin.delete()
        return Response({"message": "Admin deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# Similar views for Equipment
class EquipmentList(APIView):
    def get(self, request):
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EquipmentDetail(APIView):
    def get(self, request, pk):
        try:
            equipment = Equipment.objects.get(equipment_id=pk)
        except Equipment.DoesNotExist:
            return Response({"error": "Equipment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            equipment = Equipment.objects.get(equipment_id=pk)
        except Equipment.DoesNotExist:
            return Response({"error": "Equipment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EquipmentSerializer(equipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            equipment = Equipment.objects.get(equipment_id=pk)
        except Equipment.DoesNotExist:
            return Response({"error": "Equipment not found"}, status=status.HTTP_404_NOT_FOUND)
        equipment.delete()
        return Response({"message": "Equipment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# Similar views Maintenance
class MaintenanceList(APIView):
    def get(self, request):
        maintenances = Maintenance.objects.all()
        serializer = MaintenanceSerializer(maintenances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaintenanceDetail(APIView):
    def get(self, request, pk):
        try:
            maintenance = Maintenance.objects.get(maintenance_id=pk)
        except Maintenance.DoesNotExist:
            return Response({"error": "Maintenance not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MaintenanceSerializer(maintenance)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            maintenance = Maintenance.objects.get(maintenance_id=pk)
        except Maintenance.DoesNotExist:
            return Response({"error": "Maintenance not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MaintenanceSerializer(maintenance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            maintenance = Maintenance.objects.get(maintenance_id=pk)
        except Maintenance.DoesNotExist:
            return Response({"error": "Maintenance not found"}, status=status.HTTP_404_NOT_FOUND)
        maintenance.delete()
        return Response({"message": "Maintenance deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
