from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def display(request):
    return render(request,'display.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('counter')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password not the same')
            return redirect('signup')
    else:
        return render(request,'signup.html')

def counter(request):
    return render(request,'counter.html')

def result(request):
    text=request.GET['text']
    number_of_words=len(text.split())
    return render(request,'result.html',{'number':number_of_words})
def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
