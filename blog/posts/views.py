from django.shortcuts import render,redirect
from .models import post
from django.contrib import messages

# Create your views here.
def index(request):
    posts=post.objects.all()
    return render(request,'index.html',{'posts':posts}) 

def posts(request,pk):
    posts=post.objects.get(title=pk)
    return render(request,'post.html',{'posts':posts})
    
def addblog(request):
    return render(request,'addblog.html')

def addblogdisplay(request):
    title=request.GET['title']
    body=request.GET['description']
    posts=post.objects.create(title=title,body=body)
    posts.save();
    return redirect('index')
def deleteblog(request):
    return render(request,'deleteblog.html')

def displaydeleteblog(request):
    title=request.GET['title']
    if post.objects.filter(title=title).exists():
        posts=post.objects.get(title=title)
        posts.delete()
        return redirect('index')
    else:
        messages.info(request,'Title does not exist')
        return redirect('deleteblog')
    
        

