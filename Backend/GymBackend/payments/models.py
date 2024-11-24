from django.db import models
import uuid
from membership.models import Member

class Payment(models.Model):
    # Custom Primary Key (UUID for global uniqueness)
    payment_reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Sender's account identifier (could represent a bank account number or wallet ID)
    sender_account = models.CharField(max_length=255)
    
    # Direction of payment (credit or debit)
    payment_direction = models.CharField(max_length=50, choices=[('credit', 'Credit'), ('debit', 'Debit')])
    
    # Method used for the transaction (e.g., bank transfer, mobile wallet, etc.)
    payment_method = models.CharField(max_length=50, choices=[('cash', 'Cash'), ('credit_card', 'Credit Card'),
                                                              ('bank_transfer', 'Bank Transfer'), 
                                                              ('mobile_wallet', 'Mobile Wallet')])
    
    # Current status of the payment (e.g., pending, completed, failed)
    transaction_status = models.CharField(max_length=50, choices=[('pending', 'Pending'), 
                                                                  ('completed', 'Completed'),
                                                                  ('failed', 'Failed')])
    
    # Amount of the transaction
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Retry count to track payment retries if it fails
    retry_count = models.PositiveIntegerField(default=0)
    
    # Date of the payment
    date = models.DateField()
    
    # Foreign Key to Member model
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    def __str__(self):
        # The string representation of the Payment, providing meaningful details
        return f"Payment {self.payment_reference} - {self.amount} INR via {self.payment_method} ({self.transaction_status})"
