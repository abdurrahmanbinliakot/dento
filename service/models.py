from django.db import models

# Create your models here.
class Service(models.Model):

    service_logo_image =models.ImageField(upload_to='service/service_logo_image',blank=False)
    service_heading = models.CharField(max_length=255,blank=False)
    service_short_description = models.TextField(max_length=500,blank=False)

    def __str__(self):
        return self.service_heading
    
