from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_joining = models.DateField()
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MembershipType(models.Model):
    duration = models.PositiveIntegerField()  # Duration in months
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.duration} months - {self.cost} INR"


class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()

    def __str__(self):
        return f"Attendance for {self.member.first_name} on {self.date}"
