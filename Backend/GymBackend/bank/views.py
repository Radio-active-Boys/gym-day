from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import Payment
from .models import customer
from django.db import transaction
from django.contrib import messages
import decimal

def process_payment(request):
    if request.method == 'POST':
        form = Payment(request.POST)
        if form.is_valid():
            x = form.cleaned_data['payor']
            y = form.cleaned_data['payee']
            z = decimal.Decimal(form.cleaned_data['amount'])

            try:
                # Wrap the database operations in an atomic transaction
                with transaction.atomic():
                    # Use select_for_update to lock rows during the transaction
                    payor = customer.objects.select_for_update().get(name=x)
                    payee = customer.objects.select_for_update().get(name=y)

                    if payor.balance < z:
                        # Add error message if insufficient funds
                        messages.error(request, 'Insufficient balance in payor account.')
                        return redirect('payment')

                    # Deduct from payor
                    payor.balance -= z
                    payor.save()

                    # Add to payee
                    payee.balance += z
                    payee.save()

                    # Add success message
                    messages.success(request, 'Transaction completed successfully.')
                    return redirect('payment')  # Redirect back to the same page
            except customer.DoesNotExist:
                # Handle case where customer is not found
                messages.error(request, 'Invalid payor or payee name.')
                return redirect('payment')
    else:
        form = Payment()

    return render(request, 'index.html', {'form': form})
