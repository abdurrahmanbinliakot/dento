from django.shortcuts import render
from pricing.models import Pricing 
from about.models import *

from blog.models import Post
from django.views import generic

# Create your views here.

def index(request):
    #Pricing data
    pricing_data = Pricing.objects.all()

    # about data
    about_description = aboutDescription.objects.all()
    skill = Skill.objects.all()
    cool_fact = coolFact.objects.all()
    staff = Staff.objects.all()
    # - post
    queryset = Post.objects.filter(status=1).order_by('-created_on')



    all_data = {
        # About Data
        'about_description':about_description,
        'skills':skill,
        'cool_facts':cool_fact,
        'staffs':staff,

        #Pricing data
        'pricing_data':pricing_data,

        # - post data
        'post_list':queryset,

    }




    return render(request,'index.html',all_data)



# - to showing blog content





class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


