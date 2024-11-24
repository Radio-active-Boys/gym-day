from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Trainer, WorkoutPlan, Workout, TrainerSchedule
from .serializers import (
    TrainerSerializer,
    WorkoutPlanSerializer,
    WorkoutSerializer,
    TrainerScheduleSerializer,
)

# Trainer CRUD
class TrainerList(APIView):
    def get(self, request):
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(trainers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrainerDetail(APIView):
    def get(self, request, pk):
        try:
            trainer = Trainer.objects.get(trainer_id=pk)
        except Trainer.DoesNotExist:
            return Response({"error": "Trainer not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TrainerSerializer(trainer)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            trainer = Trainer.objects.get(trainer_id=pk)
        except Trainer.DoesNotExist:
            return Response({"error": "Trainer not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TrainerSerializer(trainer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            trainer = Trainer.objects.get(trainer_id=pk)
        except Trainer.DoesNotExist:
            return Response({"error": "Trainer not found"}, status=status.HTTP_404_NOT_FOUND)
        trainer.delete()
        return Response({"message": "Trainer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# WorkoutPlan CRUD
class WorkoutPlanList(APIView):
    def get(self, request):
        workout_plans = WorkoutPlan.objects.all()
        serializer = WorkoutPlanSerializer(workout_plans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkoutPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutPlanDetail(APIView):
    def get(self, request, pk):
        try:
            workout_plan = WorkoutPlan.objects.get(workout_plan_id=pk)
        except WorkoutPlan.DoesNotExist:
            return Response({"error": "Workout Plan not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkoutPlanSerializer(workout_plan)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            workout_plan = WorkoutPlan.objects.get(workout_plan_id=pk)
        except WorkoutPlan.DoesNotExist:
            return Response({"error": "Workout Plan not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkoutPlanSerializer(workout_plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            workout_plan = WorkoutPlan.objects.get(workout_plan_id=pk)
        except WorkoutPlan.DoesNotExist:
            return Response({"error": "Workout Plan not found"}, status=status.HTTP_404_NOT_FOUND)
        workout_plan.delete()
        return Response({"message": "Workout Plan deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# Workout CRUD
class WorkoutList(APIView):
    def get(self, request):
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutDetail(APIView):
    def get(self, request, pk):
        try:
            workout = Workout.objects.get(workout_id=pk)
        except Workout.DoesNotExist:
            return Response({"error": "Workout not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            workout = Workout.objects.get(workout_id=pk)
        except Workout.DoesNotExist:
            return Response({"error": "Workout not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkoutSerializer(workout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            workout = Workout.objects.get(workout_id=pk)
        except Workout.DoesNotExist:
            return Response({"error": "Workout not found"}, status=status.HTTP_404_NOT_FOUND)
        workout.delete()
        return Response({"message": "Workout deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# TrainerSchedule CRUD
class TrainerScheduleList(APIView):
    def get(self, request):
        schedules = TrainerSchedule.objects.all()
        serializer = TrainerScheduleSerializer(schedules, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrainerScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrainerScheduleDetail(APIView):
    def get(self, request, pk):
        try:
            schedule = TrainerSchedule.objects.get(schedule_id=pk)
        except TrainerSchedule.DoesNotExist:
            return Response({"error": "Trainer Schedule not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TrainerScheduleSerializer(schedule)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            schedule = TrainerSchedule.objects.get(schedule_id=pk)
        except TrainerSchedule.DoesNotExist:
            return Response({"error": "Trainer Schedule not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TrainerScheduleSerializer(schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            schedule = TrainerSchedule.objects.get(schedule_id=pk)
        except TrainerSchedule.DoesNotExist:
            return Response({"error": "Trainer Schedule not found"}, status=status.HTTP_404_NOT_FOUND)
        schedule.delete()
        return Response({"message": "Trainer Schedule deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
