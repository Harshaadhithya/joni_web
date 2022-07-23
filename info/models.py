from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Service(models.Model):
    title=models.CharField(max_length=60)
    description=models.CharField(max_length=300)
    main_image=models.ImageField(null=False,blank=False,upload_to='service_img/')
    
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    client_name=models.CharField(max_length=60)
    client_organisation=models.CharField(max_length=30)
    client_position=models.CharField(max_length=30)
    client_review=models.CharField(max_length=500)
    client_profile_img=models.ImageField(null=False,blank=False,upload_to='client_profile_img/')

    def __str__(self):
        if self.client_organisation:
            return '{}-{}'.format(self.client_name,self.client_organisation)
        else:
            return self.client_name

