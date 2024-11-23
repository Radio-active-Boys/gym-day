from django.db import models

# Create your models here.
from membership.models import Member

class Payment(models.Model):
    sender_account = models.CharField(max_length=255)
    payment_direction = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    transaction_status = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    retry_count = models.PositiveIntegerField(default=0)
    date = models.DateField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment {self.id} - {self.amount} INR"
