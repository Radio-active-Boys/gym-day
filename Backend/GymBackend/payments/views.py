from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def admin_list(request):
    # Temporary placeholder
    return JsonResponse({"message": "This is the admin list endpoint."})