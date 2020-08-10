from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def blogPost(request):
    return render(request,'home/blogPost.html')

def friendsPost(request):
    return render(request,'home/friendsPost.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    return render(request,'home/contact.html')