from django.shortcuts import render
from .models import Pricing
# Create your views here.

def pricing(request):
    data = Pricing.objects.all()
    return render(request, 'pricing.html',{'pricing_data':data})
