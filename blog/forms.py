from django.forms import ModelForm,Textarea
from .models import *


class BlogForm(ModelForm):
    class Meta:
        model=Blog
        fields='__all__'
        exclude=[]

    def __init__(self,*args,**kwargs):
        super(BlogForm,self).__init__(*args,**kwargs)
        self.fields['author'].widget.attrs.update({'class':'form-select'})
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['cover_image'].widget.attrs.update({'class':'form-control'})
        self.fields['tags'].widget.attrs.update({'class':'select-item form-control'})