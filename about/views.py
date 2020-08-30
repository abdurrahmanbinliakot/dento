from django.shortcuts import render
from .models import aboutDescription, Skill, coolFact, Staff
# Create your views here.

def about(request):
    about_description = aboutDescription.objects.all()
    skill = Skill.objects.all()
    cool_fact = coolFact.objects.all()
    staff = Staff.objects.all()

    all_data = {
        'about_description':about_description,
        'skills':skill,
        'cool_facts':cool_fact,
        'staffs':staff
    }

    return render(request,'about.html',all_data)