from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={}

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].widget.attrs.update({'class':'form-control'})

class UpdateProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=['user','role','verified','username']

    def __init__(self,*args,**kwargs):
        super(UpdateProfileForm,self).__init__(*args,**kwargs)
        
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['profile_image'].widget.attrs.update({'class':'form-control'})
    