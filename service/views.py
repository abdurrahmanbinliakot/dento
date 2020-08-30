from django.shortcuts import render
from .models import Service
# Create your views here.

def service(request):
    service_data ={'service_data':Service.objects.all()} 
    return render(request, 'service.html',service_data)