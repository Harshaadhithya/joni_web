from distutils.command.upload import upload
from email import message
from email.policy import default
from math import fabs
from django.db import models

# Create your models here.

class Service(models.Model):
    title=models.CharField(max_length=60)
    short_title=models.CharField(max_length=10,null=False,blank=False)
    description=models.CharField(max_length=1500)
    main_image=models.ImageField(null=False,blank=False,upload_to='service_img/')
    main_page_link=models.URLField(max_length=2000,null=True,blank=True)
    
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    client_name=models.CharField(max_length=60)
    client_organisation=models.CharField(max_length=30,null=True,blank=True)
    client_position=models.CharField(max_length=30,null=True,blank=True)
    client_review=models.CharField(max_length=500)
    client_profile_img=models.ImageField(default='client_profile_img/profile_img.png',upload_to='client_profile_img/')
    created_at=models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        if self.client_organisation:
            return '{}-{}'.format(self.client_name,self.client_organisation)
        else:
            return self.client_name

class Enquiry(models.Model):
    service_list=Service.objects.all()
    # service_choices=[]
    # for service in service_list:
    #     choice_tuple=(f'{service}',f'{service}')
    #     service_choices.append(choice_tuple)
    # service_choices.append(('other','other'))
    service_choices=(
        ('App Development','App Development'),
        ('Web Development','Web Development'),
        ('Search Engine Optimization','Search Engine Optimization'),
        ('Search Engine Marketing','Search Engine Marketing'),
        ('App Store Optimization','App Store Optimization'),
        ('Social Media Marketing','Social Media Marketing'),
        ('Other','Other')
        )
    
    name=models.CharField(max_length=120)
    email=models.EmailField()
    mobile=models.PositiveBigIntegerField(null=True,blank=True)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=0)
    enquired_for=models.CharField(max_length=100,null=True,blank=True,choices=service_choices)

    def __str__(self):
        return self.name

