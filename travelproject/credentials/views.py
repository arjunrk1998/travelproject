from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user credentials')
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        gmail=request.POST['emailid']
        password=request.POST['password']
        password2=request.POST['password1']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username existed')
                return redirect('register')
            elif User.objects.filter(email=gmail).exists():
                messages.info(request,'email existed')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=gmail,first_name=fname,last_name=lname)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password mismatched')
            return redirect('register')
        return redirect('/')

    return render (request,'register.html')

def logout (request):
    auth.logout(request)
    return redirect('/')