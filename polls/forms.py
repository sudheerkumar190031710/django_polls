from asyncio.windows_events import NULL
from multiprocessing.sharedctypes import Value
from django import forms
from django.forms import widgets

class register(forms.Form):
    gender_choices=(('1','Male'),('2','Female'),('3','Others'))
    username=forms.CharField()
    email=forms.EmailField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    phone_number=forms.IntegerField()
    gender=forms.CharField(widget=forms.RadioSelect(choices=gender_choices,attrs={'class': 'gender '}))
    address=forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 4}))
    Your_profile_pic=forms.ImageField(required=False)
    password=forms.CharField(widget=forms.PasswordInput())

class userlogin(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

class createpoll(forms.Form):
    question=forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}))
    opt1=forms.CharField()
    opt2=forms.CharField()
    opt3=forms.CharField()
    opt4=forms.CharField()

class userdetails(forms.Form):
    gender_choices=(('1','Male'),('2','Female'),('3','Others'))
    username=forms.CharField()
    email=forms.EmailField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    phone_number=forms.IntegerField()
    gender=forms.CharField(widget=forms.RadioSelect(choices=gender_choices,attrs={'class': 'gender '}))
    address=forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 4}))