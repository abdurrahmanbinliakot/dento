from django.db import models

# Create your models here.
class Pricing(models.Model):
    service_names = models.TextField(max_length=500,blank=False)
    stage = models.IntegerField(blank=False,default=0)
    price = models.IntegerField(blank=False,default=0)

    def __str__(self):
        return self.service_names