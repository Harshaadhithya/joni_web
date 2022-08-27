from pyexpat import model
from django.db import models
from users.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200,unique=True)
    url_title=models.CharField(max_length=200,unique=True,null=True)
    author=models.ForeignKey(Profile,null=True,blank=False,on_delete=models.CASCADE)
    description=models.CharField(null=True,blank=True,max_length=300)
    cover_image=models.ImageField(null=False,blank=False,upload_to='blog_cover/')
    tags=models.ManyToManyField('Tag',blank=True)
    body=RichTextUploadingField()
    # vote_total=models.IntegerField(default=0,blank=True,null=True)
    # vote_ratio=models.IntegerField(default=0,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
