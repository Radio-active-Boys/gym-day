from django.db import models

# Create your models here.
from membership.models import Member

class Trainer(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class WorkoutPlan(models.Model):
    name = models.CharField(max_length=255)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} for {self.member.first_name}"

class Workout(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    reps = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()  # Duration in minutes
    rest_period = models.PositiveIntegerField()  # Rest period in seconds

    def __str__(self):
        return f"{self.name} - {self.workout_plan.name}"

class TrainerSchedule(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    is_leave = models.BooleanField(default=False)

    def __str__(self):
        return f"Schedule for {self.trainer.name} on {self.date}"
