from email.policy import default
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    role_types=(
        ('admin','admin'),
        ('other','other')
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    role=models.CharField(max_length=50,choices=role_types,default='other')
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=400,null=True,blank=True)
    username=models.CharField(max_length=200,null=True,blank=True)
    profile_image=models.ImageField(null=False,blank=False,upload_to='client_profile_img/',default='client_profile_img/profile_img.png')
    verified=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

