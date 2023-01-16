from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.email

class chairmen(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    username= models.CharField(max_length=30)
    contac = models.CharField(max_length=30)
    pic = models.FileField(upload_to='media/images/',default='media/set.png')

    
    def __str__(self):
        return self.username

class Member(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    family_member = models.CharField(max_length=30)
    job_location = models.CharField(max_length=30)
    block_no = models.CharField(max_length=30)
    house_no = models.CharField(max_length=30)
    pic = models.FileField(upload_to='media/images/',default='media/set.png')

    
    def __str__(self):
        return self.firstname

class Notice(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    descriptions = models.TextField()
    pic = models.FileField(upload_to='media/images/',default='media/set.png',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    name = models.CharField(max_length=30)
    pic = models.FileField(upload_to='media/video/',default='media/soceity.mp4',blank=True,null=True)
   
    

    