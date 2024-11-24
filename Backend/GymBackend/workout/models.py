from django.db import models
from membership.models import Member

class Trainer(models.Model):
    trainer_id = models.CharField(max_length=15, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.trainer_id:
            # Generate ID: "TR-{First3LettersName}-{SpecialtyAbbrev}-{Count}"
            specialty_abbrev = ''.join(word[0] for word in self.specialty.split()[:2]).upper()
            count = Trainer.objects.filter(specialty__iexact=self.specialty).count() + 1
            self.trainer_id = f"TR-{self.name[:3].upper()}-{specialty_abbrev}{str(count).zfill(3)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    workout_plan_id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=255)
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="workout_plans"
    )
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workout_plans"
    )

    def save(self, *args, **kwargs):
        if not self.workout_plan_id:
            # Generate ID: "WP-{MemberID}-{YYYYMMDD}-{Count}"
            today = datetime.date.today().strftime("%Y%m%d")
            count = WorkoutPlan.objects.filter(
                member=self.member,
                workout_plan_id__contains=today
            ).count() + 1
            self.workout_plan_id = f"WP-{self.member.id}-{today}-{str(count).zfill(3)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} for {self.member.first_name}"

class Workout(models.Model):
    workout_id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    workout_plan = models.ForeignKey(
        WorkoutPlan,
        on_delete=models.CASCADE,
        related_name="workouts"
    )
    name = models.CharField(max_length=255)
    reps = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()  # Duration in minutes
    rest_period = models.PositiveIntegerField()  # Rest period in seconds

    def save(self, *args, **kwargs):
        if not self.workout_id:
            # Generate ID: "WO-{WorkoutPlanID}-{Count}"
            count = Workout.objects.filter(workout_plan=self.workout_plan).count() + 1
            self.workout_id = f"WO-{self.workout_plan.workout_plan_id}-{str(count).zfill(2)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.workout_plan.name}"

class TrainerSchedule(models.Model):
    schedule_id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name="schedules"
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    is_leave = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.schedule_id:
            # Generate ID: "SC-{TrainerID}-{YYYYMMDD}-{Count}"
            count = TrainerSchedule.objects.filter(trainer=self.trainer, date=self.date).count() + 1
            self.schedule_id = f"SC-{self.trainer.trainer_id}-{self.date.strftime('%Y%m%d')}-{str(count).zfill(2)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Schedule for {self.trainer.name} on {self.date}"
