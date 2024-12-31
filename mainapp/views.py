from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


def demo(request):
    return render(request,"index.html")


def login_user(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        user = authenticate(request,username=username,password= password)
        if user is not None:
            login(request,user)            
            return render(request,"index.html",{'username':username})
        else:
            
            return redirect('login_user')
    return render (request,"login.html")

def signup(request):
    
    if request.method == 'POST':
        username = request.POST['uname']
        email = request.POST['mail']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username,email=email,password= password1)
            user.save()
            return redirect('demo')
    return render(request,"signup.html")    


