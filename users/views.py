from cmath import log
import imp
from logging import warning
from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.


def signin(request):
    if request.user.is_authenticated:
        return redirect('home') 

    if request.method=='POST':
        entered_username=request.POST['username']
        entered_password=request.POST['password']
        try:
            user=User.objects.get(username=entered_username)
        except:
            messages.error(request,'Username does not exists')
        user=authenticate(request,username=entered_username,password=entered_password)

        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        else:
            messages.error(request,'Username or Password is incorrect')

    page='login'
    context={'page':page}
    return render(request,'users/signup.html',context)

@login_required(login_url='signin')
def logout_user(request):
    logout(request)
    messages.success(request,'User was logged out!')
    return redirect('signin')

def signup(request):
    page='signup'
    form=CustomUserCreationForm()
    form=CustomUserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'User was created successfully')
            login(request,user)
            return redirect('update_profile')
        else:
            messages.error(request,'something went wrong')

            
    context={'page':page,'form':form}
    return render(request,'users/signup.html',context)

@login_required(login_url='signin')
def update_profile(request):
    profile_data=request.user.profile
    form=UpdateProfileForm(instance=profile_data)
    if request.method=='POST':
        form=UpdateProfileForm(request.POST,request.FILES,instance=profile_data)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile updated Successfully!")
    context={'form':form}
    return render(request,'users/edit_my_account.html',context)

@login_required(login_url='signin')
def user_list(request):
    if request.user.profile.role=='admin':
        profiles=Profile.objects.all()
        context={'profiles':profiles}
        return render(request,'users/user_list.html',context)
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')

@login_required(login_url='signin')
def give_admin_rights(request,pk):
    if request.user.profile.role=='admin':
        profile_obj=Profile.objects.get(id=pk)
        profile_obj.role='admin'
        profile_obj.verified=True
        profile_obj.save()
        messages.success(request,f'{profile_obj.name} is now an admin!')
        return redirect('user_list')
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')

@login_required(login_url='signin')
def remove_admin_rights(request,pk):
    if request.user.profile.role=='admin':
        profile_obj=Profile.objects.get(id=pk)
        profile_obj.role='other'
        profile_obj.verified=False
        profile_obj.save()
        messages.success(request,f'{profile_obj.name} is not an admin anymore!')
        return redirect('user_list')
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')

@login_required(login_url='signin')
def delete_user_profile(request,pk):
    if request.user.profile.role=='admin':
        profile_obj=Profile.objects.get(id=pk)
        print(profile_obj,profile_obj.user)
        user_obj=profile_obj.user
        user_obj.delete()
        messages.success(request,f'{profile_obj.name} is Deleted!')
        return redirect('user_list')
    else:
        messages.warning(request,"You are not authorised to view this page!")
        return redirect('home')