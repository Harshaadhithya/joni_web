import email
from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from .models import Profile

def user_created_reciever(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            username=instance.username,
            name=instance.username,
            email=instance.email
        )

def profile_delete_reciever(sender,instance,**kwargs):
    user_obj=instance.user
    user_obj.delete



post_save.connect(user_created_reciever,sender=User)
# post_delete.connect(profile_delete_reciever,sender=Profile)