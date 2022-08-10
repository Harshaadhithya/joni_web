import email
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from threading import Thread
from django.contrib.auth.decorators import login_required

from django.urls import is_valid_path
from .forms import *

from django.contrib import messages


class EmailThread(Thread):
    def __init__(self,email_content):
        self.email_content=email_content
        Thread.__init__(self)

    def run (self):
        try:
            send_mail(subject=f'Enquiry Mail',from_email='joniweb12@gmail.com',message=self.email_content,recipient_list=['reachus@jonisolutions.com'])
        except:
            print("failed to send mail")

# Create your views here.
def home(request):
    context={'page':'home'}
    services=Service.objects.all()
    testimonials=Testimonial.objects.all()
    context['services']=services
    context['testimonials']=testimonials
    return render(request,'info/index.html',context)

def about_us(request):
    context={'page':'about_us'}
    return render(request,'info/about.html',context)

def dummy(request):
    return HttpResponse

def services_page(request):
    context={'page':'services'}
    services=Service.objects.all()
    context['services']=services
    return render(request,'info/services.html',context)

def contact_us(request):
    context={'page':'contact_us'}
    if request.method=='POST':
        print('mail sent')
        name=request.POST['name']
        email_address=request.POST['email_address']
        mobile=request.POST['mobile']
        message=request.POST['message']
        if not mobile:
            email_content=f'Name : {name}\nEmail : {email_address}\n\n'
        else:
            email_content=f'Name : {name}\nEmail : {email_address}\nMobile : {mobile}\n\n'
        email_content+=message
        
        # obj1=EmailThread(name,email_address,mobile,message)
        # obj1.start()
        if mobile=='':
            mobile=None
        EmailThread(email_content=email_content).start()
        try:
            enquiry_obj=Enquiry.objects.create(name=name,email=email_address,mobile=mobile,message=message)
            messages.success(request,'We have received your information. We will get in touch with you soon.')
        except:
            pass
        # send_mail(subject=f'Enquiry Mail from {name}-{mobile}',from_email='joniweb12@gmail.com',message=message,recipient_list=['harshaadhithya1234@gmail.com'])
        
    return render(request,'info/contact.html',context)

def separate_service(request,service_name):
    return render(request,f'info/{service_name}.html')

@login_required(login_url='signin')
def enquiry_list(request):
    if request.user.profile.role=='admin':
        enquiry_list=Enquiry.objects.all().order_by('-created')
        context={'enquiry_list':enquiry_list}
        return render(request,'info/enquiry_list.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')

@login_required(login_url='signin')
def mark_as_read(request,pk):
    if request.user.profile.role=='admin':
        enquiry_obj=Enquiry.objects.get(id=pk)
        enquiry_obj.is_read=True
        enquiry_obj.save()
        return redirect('enquiry_list')
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')   


@login_required(login_url='signin')
def manage_service(request):
    if request.user.profile.role=='admin':
        services=Service.objects.all()
        context={'services':services}
        return render(request,'info/manage_service.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')   

@login_required(login_url='signin')
def add_service(request):
    if request.user.profile.role=='admin':
        form=ServiceForm()
        if request.method=='POST':
            form=ServiceForm(request.POST,request.FILES)
            for field in form:
                print(field.errors,field.name)
            # if form.is_valid():
            
            if form.is_valid():
                print("form is valid")
                service=form.save(commit=False)
                service.short_title=service.short_title.lower()
                service.save()
                messages.success(request,"Service Added Successfully!")

            else:
                messages.error(request,"Something Went Wrong!")
            return redirect('manage_service')
        context={'form':form,'page':'service'}
        return render(request,'info/form.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')   

@login_required(login_url='signin')
def edit_service(request,pk):
    if request.user.profile.role=='admin':
        service_obj=Service.objects.get(id=pk)
        form=ServiceForm(instance=service_obj)
        if request.method=='POST':
            form=ServiceForm(request.POST,request.FILES,instance=service_obj)
            for field in form:
                print(field.errors,field.name)        
            if form.is_valid():
                print("form is valid")
                form.save()
                messages.success(request,"Service Updated Successfully!")

            else:
                messages.error(request,"Something Went Wrong!")
            return redirect('manage_service')
        context={'form':form,'page':'service'}
        return render(request,'info/form.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')   

@login_required(login_url='signin')
def delete_service(request,pk):
    if request.user.profile.role=='admin':
        service_obj=Service.objects.get(id=pk)
        try:
            service_obj.delete()
            messages.success(request,"Service Added Successfully!")
        except:
            messages.error(request,"Something Went Wrong!")
        return redirect('manage_service')
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')   

@login_required(login_url='signin')
def manage_testimonials(request):
    if request.user.profile.role=='admin':
        testimonials=Testimonial.objects.all()
        context={'testimonials':testimonials}
        return render(request,'info/manage_testimonials.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')   

@login_required(login_url='signin')
def add_testimonial(request):
    if request.user.profile.role=='admin':
        form=TestimonialForm()
        if request.method=='POST':
            form=TestimonialForm(request.POST,request.FILES)
            for field in form:
                print(field.label,field.errors)
            if form.is_valid():
                form.save()
                messages.success(request,"Testimonial Added Successfully!")
                return redirect('manage_testimonials')
            else:
                messages.error(request,"Something Went Wrong!")
        context={'form':form,'page':'testimonial'}
        return render(request,'info/form.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')   

@login_required(login_url='signin')
def edit_testimonial(request,pk):
    if request.user.profile.role=='admin':
        testimonial_obj=Testimonial.objects.get(id=pk)
        form=TestimonialForm(instance=testimonial_obj)
        if request.method=='POST':
            form=TestimonialForm(request.POST,request.FILES,instance=testimonial_obj)
            for field in form:
                print(field.errors,field.name)        
            if form.is_valid():
                print("form is valid")
                form.save()
                messages.success(request,"Testimonial Updated Successfully!")
            else:
                print("form is not valid")
                messages.error(request,"Something Went Wrong!")
            return redirect('manage_testimonials')
        context={'form':form,'page':'testimonial'}
        return render(request,'info/form.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')   

@login_required(login_url='signin')
def delete_testimonial(request,pk):
    if request.user.profile.role=='admin':
        testimonial_obj=Testimonial.objects.get(id=pk)
        try:
            testimonial_obj.delete()
            messages.success(request,"Testimonial Deleted Successfully")
        except:
            messages.error(request,"Something Went Wrong")

        return redirect('manage_testimonials')
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')   

@login_required(login_url='signin')
def update_enquiry(request,pk):
    if request.user.profile.role=='admin':
        page='Enquiry'
        enquiry_obj=Enquiry.objects.get(id=pk)
        form=EnquiryForm(instance=enquiry_obj)
        if request.method=='POST':
            form=EnquiryForm(request.POST,instance=enquiry_obj)
            if form.is_valid():
                form.save()
                messages.success(request,"Enquiry Updated Successfully !")
            else:
                messages.error(request,"Something Went Wrong !")
            return redirect('enquiry_list')
        context={'form':form,'page':page}
        return render(request,'info/form.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home') 

def sitemap(request):
    return HttpResponse(open('sitemap.xml').read(), content_type='text/xml')  

def robots(request):
    return HttpResponse(open('Robots.txt').read(), content_type='text')  



