from django.db import models

# Create your models here.
class aboutDescription(models.Model):
    about_description = models.TextField(max_length=255,blank=False,default='Write here an about descriptions')
    about_thumbnail =models.ImageField(upload_to='about/about_thumbnail',blank=False)
    def __str__(self):
        return self.about_description

class Skill(models.Model):
    skill_name = models.CharField(max_length=100, blank= False)
    amount_of_skill = models.SmallIntegerField(blank=False, default=0)
    def __str__(self):
        return self.skill_name
    

class coolFact(models.Model):

    ICON_TYPE = (
    ('icon_heart_alt','Heart'),
    ('icon_genius','Genius'),
    ('icon_book_alt','Book'),
    ('icon_id','Icon Id')
    
    )

    fact_name = models.CharField(max_length=100,blank=False)
    fact_icon = models.CharField(max_length=20,choices=ICON_TYPE)
    counter = models.IntegerField(blank=False, default=0)
    plus = models.BooleanField(blank=False, default=0)
   
    def __str__(self):
        return self.fact_name
    

class Staff(models.Model):
    name =models.CharField(max_length=255,blank=False)
    designation =models.CharField(max_length=255,blank=False)
    photo = models.ImageField(upload_to='team_member_photo',blank=False)
    facebook_profile = models.URLField()
    twitter_profile = models.URLField()
    google_plus_profile = models.URLField()

    def __str__(self):
        return self.name
    