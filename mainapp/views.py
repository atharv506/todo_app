from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from mainapp.models import TODO
from  mainapp.forms import TODOform


#def main(request):
 #   return render(request,"index.html")
def main(request):
    form = TODOform()
    if request.user.is_authenticated:
        return render(request, "index.html", context= {'username': request.user.username ,'form':form})
    else:
        return render(request, "index.html")   



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
            return redirect('login_user')
        else:
            messages.warning(request, "Passwords do not match. Please try again.")
    return render(request,"signup.html")    


def signout(request):
    logout(request)
    return redirect('login_user')
    