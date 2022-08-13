from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render,redirect

from info.models import Service
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.

def blog_home(request):
    blogs=Blog.objects.filter().order_by('-created')
    context={'blogs':blogs,'page':'blogs'}
    return render(request,'blog/blog_home.html',context)

def sample_blog(request):
    context={}
    return render(request,'blog/sample_blog.html',context)


@login_required(login_url='signin')
def create_blog(request):
    if request.user.profile.role=='admin':
        page='Create New Blog'
        form=BlogForm(initial={'author': request.user.profile})
        if request.method=='POST':
            form=BlogForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"Blog Posted Successfully!")
                return redirect('blog_home')
            else:
                messages.error(request,"Failed to Post!")
        context={'form':form,'page':page}
        return render(request,'blog/blog_form.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')

def view_blog(request,pk):
    
    blog_obj=Blog.objects.get(id=pk)
    tags=blog_obj.tags.all()
    related_blogs=[]
    for tag in tags:
        related_blogs+=Blog.objects.distinct().filter(tags__name__icontains=tag.name)
    related_blogs=list(set(related_blogs))
    services=Service.objects.all()
    context={'blog_obj':blog_obj,'related_blogs':related_blogs,'services':services}
    return render(request,'blog/view_blog.html',context)

@login_required(login_url='signin')
def manage_blogs(request):
    if request.user.profile.role=='admin':
        blogs=Blog.objects.all()
        context={'blogs':blogs}
        return render(request,'blog/manage_blogs.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')

@login_required(login_url='signin')
def update_blog(request,pk):
    if request.user.profile.role=='admin':
        blog_obj=Blog.objects.get(id=pk)
        page=f'update {blog_obj.title}'
        form=BlogForm(instance=blog_obj)
        if request.method=='POST':
            form=BlogForm(request.POST,request.FILES,instance=blog_obj)
            if form.is_valid():
                form.save()
                messages.success(request,"Blog Updated Successfully!")
                return redirect('blog_home')
            else:
                messages.error(request,"Failed to Update!")
        context={'form':form,'page':page}
        return render(request,'blog/blog_form.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')
