from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render,redirect

from info.models import Service
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from info.models import Page


# Create your views here.

# @login_required(login_url='signin')
def blog_home(request):
    blogs=Blog.objects.filter().order_by('-created')
    context={'blogs':blogs}
    page_obj,_=Page.objects.get_or_create(name='blogs')
    context['meta_title']=page_obj.meta_title
    context['meta_description']=page_obj.meta_description
    context['meta_keywords']=page_obj.meta_keywords
    return render(request,'blog/blog_home.html',context)

def sample_blog(request):
    context={}
    return render(request,'blog/sample_blog.html',context)


@login_required(login_url='signin')
def create_blog(request):
    if request.user.profile.role=='admin':
        page='Create New Blog'
        form=BlogForm(initial={'author': request.user.profile})
        tags=Tag.objects.all()
        if request.method=='POST':
            post=request.POST.copy()
            tag_list=[]
            for tag_id in request.POST.getlist('tags'):
                try:
                    if Tag.objects.filter(id=tag_id).exists(): #if this arises any error then there exist no such tag, this error is arised because we will be getting id if already tag is exist, else we will get the name of the new tag entered and when we try to match with tag id it causes an error.
                        pass
                    
                    else:
                        tag_obj=Tag.objects.create(name=tag_id)
                        tag_id=tag_obj.id

                except:
                    tag_obj=Tag.objects.create(name=tag_id)
                    tag_id=tag_obj.id
                tag_list.append(tag_id)

            post.setlist('tags', tag_list)
            request.POST=post
            print(request.POST)
            # print(request.POST)
            form=BlogForm(request.POST,request.FILES)
            # print("tags",request.POST.get('tags'))
            # print(request.POST.getlist('tags'))
            
            print("before is valid")      
            if form.is_valid():
                print("inside is valid")
                blog_obj=form.save(commit=False)
                blog_obj.url_title=blog_obj.title.replace(" ","-")
                blog_obj.save()
                print("after save")
                messages.success(request,"Blog Posted Successfully!")
                return redirect('blog_home')
            else:
                messages.error(request,"Failed to Post!")
        context={'form':form,'page':page,'tags':tags}
        return render(request,'blog/blog_form.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')


def view_blog(request,pk):
    try:
        blog_obj=Blog.objects.get(url_title=pk)
        tags=blog_obj.tags.all()
        related_blogs=[]
        for tag in tags:
            print(blog_obj.id)
            related_blogs+=Blog.objects.distinct().filter(tags__name__icontains=tag.name).exclude(id=blog_obj.id)
        related_blogs=list(set(related_blogs))
        if len(related_blogs)<1:
            related_blogs=Blog.objects.filter().exclude(id=blog_obj.id)[:10]
        services=Service.objects.all()
        context={'blog_obj':blog_obj,'related_blogs':related_blogs,'services':services}
        return render(request,'blog/view_blog.html',context)
    except Exception as e:
        print(e)
        messages.error(request,"Page not found!")
        return redirect('home')

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
            post=request.POST.copy()
            tag_list=[]
            for tag_id in request.POST.getlist('tags'):
                try:
                    if Tag.objects.filter(id=tag_id).exists(): #if this arises any error then there exist no such tag, this error is arised because we will be getting id if already tag is exist, else we will get the name of the new tag entered and when we try to match with tag id it causes an error.
                        pass
                    
                    else:
                        tag_obj=Tag.objects.create(name=tag_id)
                        tag_id=tag_obj.id

                except:
                    tag_obj=Tag.objects.create(name=tag_id)
                    tag_id=tag_obj.id
                tag_list.append(tag_id)

            post.setlist('tags', tag_list)
            request.POST=post
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
