from django.forms import ModelForm,Textarea
from .models import *
from django import forms


class BlogForm(ModelForm):
    # tags1=forms.MultipleChoiceField((choices=[(t, t) for t in Tag.objects
    #             .order_by().values_list('name', flat=True).distinct()],
    #         widget=forms.SelectMultiple(attrs={'class': 'form-select'}))
    class Meta:
        model=Blog
        fields='__all__'
        exclude=['url_title']

    def __init__(self,*args,**kwargs):
        super(BlogForm,self).__init__(*args,**kwargs)
        self.fields['author'].widget.attrs.update({'class':'form-select'})
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['cover_image'].widget.attrs.update({'class':'form-control'})
        self.fields['tags'].widget.attrs.update({'class':'select-item form-control'})

    # def save(self,commit=True):
    #     return super(BlogForm,self).save(commit=commit)