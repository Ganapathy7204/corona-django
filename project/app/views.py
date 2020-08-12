from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Contact
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage

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


def handlelogout(request):
    logout(request)
    return render(request,'home/index.html')


def blogPost(request):
    return render(request,'home/blogPost.html')

def friendsPost(request):
    return render(request,'home/friendsPost.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('num')
        desc=request.POST.get('desc')
        from_email=settings.EMAIL_HOST_USER
        # print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        connection=mail.get_connection()
        connection.open()
        email1=mail.EmailMessage(name,desc,from_email,['aneesurrehman423@gmail.com'],connection=connection)
        connection.send_messages([email1])
        connection.close()
        # https://myaccount.google.com/lesssecureapps
        # allow less secure app 
        return HttpResponse("Record has been sent")





        return redirect('/')

    return render(request,'home/contact.html')