from django.db import models
from django.utils import timezone

class MembershipType(models.Model):
    membership_type_id = models.CharField(max_length=15, primary_key=True, blank=True)  # Fixed length 15
    duration = models.PositiveIntegerField()  # Duration in months
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.membership_type_id:  # Generate the ID if it doesn't exist
            self.membership_type_id = f"MT-{str(self.duration).zfill(3)}-{str(int(self.cost)).zfill(4)}"
        super(MembershipType, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.duration} months - {self.cost} INR"

class Member(models.Model):
    member_id = models.CharField(max_length=15, primary_key=True, blank=True)  # Fixed length 15
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_joining = models.DateField()
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    membership_type = models.ForeignKey(MembershipType, on_delete=models.SET_NULL, null=True)  # Foreign key to MembershipType

    def save(self, *args, **kwargs):
        if not self.member_id:  # Generate the ID if it doesn't exist
            year_of_joining = self.date_of_joining.year
            last_name_initials = self.last_name[:3].upper()
            # Example: SMT-2023-001, for first member of the year 2023 with last name starting with 'SMT'
            member_count = Member.objects.filter(date_of_joining__year=year_of_joining).count() + 1
            self.member_id = f"{last_name_initials}-{year_of_joining}-{str(member_count).zfill(3)}"
        super(Member, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Attendance(models.Model):
    attendance_id = models.CharField(max_length=25, primary_key=True, blank=True)  # Fixed length 25
    member = models.ForeignKey(Member, on_delete=models.CASCADE)  # Foreign key to Member
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()

    def save(self, *args, **kwargs):
        if not self.attendance_id:  # Generate the ID if it doesn't exist
            member_prefix = self.member.member_id  # Get the member's ID
            # Example: SMT-2023-001-20231124-01 for the first attendance of member SMT-2023-001 on 2023-11-24
            attendance_count = Attendance.objects.filter(member=self.member, date=self.date).count() + 1
            self.attendance_id = f"{member_prefix}-{self.date.strftime('%Y%m%d')}-{str(attendance_count).zfill(2)}"
        super(Attendance, self).save(*args, **kwargs)

    def __str__(self):
        return f"Attendance for {self.member.first_name} on {self.date}"

