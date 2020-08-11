from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'home/index.html')


def handleSignup(request):
    if request.method == "POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if len(username)>10:
            return HttpResponse("Username should be less that 10 characters")
        if not username.isalnum():
            return HttpResponse("Username should contain only letters and numbers")
        if pass1!=pass2:
            return HttpResponse("passsword is Incorrect")

        myuser= User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return redirect('/')


    return render(request,'home/index.html')

def handleLogin(request):

    if request.method == "POST":
        loginusername=request.POST['username']
        loginpassword=request.POST['pass1']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            return HttpResponse("login success")
        else:
            return HttpResponse("invalid credentials")    
 
    
    return render(request,'home/index.html')


def blogPost(request):
    return render(request,'home/blogPost.html')

def friendsPost(request):
    return render(request,'home/friendsPost.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    return render(request,'home/contact.html')