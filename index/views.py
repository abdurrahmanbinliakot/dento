from django.shortcuts import render
from pricing.models import Pricing 
from about.models import *
# Create your views here.

def index(request):
    #Pricing data
    pricing_data = Pricing.objects.all()

    # about data
    about_description = aboutDescription.objects.all()
    skill = Skill.objects.all()
    cool_fact = coolFact.objects.all()
    staff = Staff.objects.all()
    all_data = {
        # About Data
        'about_description':about_description,
        'skills':skill,
        'cool_facts':cool_fact,
        'staffs':staff,

        #Pricing data
        'pricing_data':pricing_data

    }




    return render(request,'index.html',all_data)