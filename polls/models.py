from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserDetails(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    gender=models.PositiveSmallIntegerField()
    phone_number=models.PositiveBigIntegerField()
    address=models.TextField()
    dp=models.ImageField(upload_to="dp/",null=True,blank=True)

class PollQuestions(models.Model):
    poll_id=models.AutoField(primary_key=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.TextField()
    opt1=models.CharField(max_length=30)
    opt2=models.CharField(max_length=30)
    opt3=models.CharField(max_length=30)
    opt4=models.CharField(max_length=30)

class PollAnswer(models.Model):
    poll_id=models.ForeignKey(PollQuestions,on_delete=models.CASCADE)
    
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    answer=models.SmallIntegerField()

