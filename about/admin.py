from django.contrib import admin
from .models import aboutDescription, Skill, coolFact, Staff

# Register your models here.

admin.site.register(aboutDescription)
admin.site.register(Skill)
admin.site.register(coolFact)
admin.site.register(Staff)