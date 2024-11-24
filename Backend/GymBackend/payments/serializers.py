from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    # Include the member ID field in the response as well
    member_id = serializers.IntegerField(source='member.id', read_only=True)

    class Meta:
        model = Payment
        fields = ['payment_reference', 'sender_account', 'payment_direction', 'payment_method', 
                  'transaction_status', 'amount', 'retry_count', 'date', 'member_id']
