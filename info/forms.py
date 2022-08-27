from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm,Textarea
from .models import *


class EnquiryForm(ModelForm):
    class Meta:
        model=Enquiry
        fields='__all__'
        exclude=['is_read']

    def __init__(self,*args,**kwargs):
        super(EnquiryForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control big-textarea'})
        self.fields['mobile'].widget.attrs.update({'class':'form-control'})
        self.fields['message'].widget.attrs.update({'class':'form-control'})
        self.fields['enquired_for'].widget.attrs.update({'class':'form-select'})


class ServiceForm(ModelForm):
    class Meta:
        model=Service
        fields='__all__'
        labels={
            'main_image':'Cover Image',
        }
        exclude=['main_page_link']
        
        widgets = {
            'description': Textarea(attrs={'rows': 8}),
        }

    def __init__(self,*args,**kwargs):
        super(ServiceForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['url_title'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control big-textarea'})
        self.fields['short_title'].widget.attrs.update({'class':'form-control'})
        self.fields['main_image'].widget.attrs.update({'class':'form-control'})


class TestimonialForm(ModelForm):
    class Meta:
        model=Testimonial
        fields='__all__'

        widgets = {
                'client_review': Textarea(attrs={'rows': 8}),
            }

    def __init__(self,*args,**kwargs):
        super(TestimonialForm,self).__init__(*args,**kwargs)
        self.fields['client_name'].widget.attrs.update({'class':'form-control'})
        self.fields['client_organisation'].widget.attrs.update({'class':'form-control'})
        self.fields['client_position'].widget.attrs.update({'class':'form-control'})
        self.fields['client_review'].widget.attrs.update({'class':'form-control big-textarea'})
        self.fields['client_profile_img'].widget.attrs.update({'class':'form-control'})


