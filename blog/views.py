from django.shortcuts import render

# Create your views here.

def blog_home(request):
    context={}
    return render(request,'blog/blog_home.html',context)
