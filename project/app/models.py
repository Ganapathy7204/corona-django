from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    desc=models.TextField()
    def __str__(self):
        return self.name
    
class Friendspost(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    author=models.CharField(max_length=50)
    img=models.ImageField(upload_to='friends',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.author
    
class Adminspost(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    author=models.CharField(max_length=50)
    img=models.ImageField(upload_to='friends',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    

    def __str__(self):
        return self.author

    # pip install Pillow    
    
