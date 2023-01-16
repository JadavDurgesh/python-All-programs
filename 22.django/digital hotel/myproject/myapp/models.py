from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

    def __str__(self):
        return  self.email

class Chairmen(models.Model):
    urser_id = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    pic = models.FileField(upload_to='media/images/',default='media/images/set.jpg')

    def __str__(self):
        return self.username

class Member(models.Model):
    urser_id      = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname     = models.CharField(max_length=30)
    lastname      = models.CharField(max_length=30)
    contact_no    = models.CharField(max_length=30)
    family_member = models.CharField(max_length=30)
    occupation    = models.CharField(max_length=30)
    block_no      = models.CharField(max_length=30)
    house_no      = models.CharField(max_length=30)
    pic           = models.FileField(upload_to='media/images/',default='media/images/set.jpg')

    def __str__(self):
        return self.firstname


class Notice(models.Model):
    name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    titel = models.CharField(max_length=100)
    descrition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titel

class Event(models.Model):
    name = models.CharField(max_length=30)
    video = models.FileField(upload_to='media/video/',default='media/video/hotel.mp4' ,null=True,blank=True)
   



