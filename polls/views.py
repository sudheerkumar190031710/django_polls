from asyncio.windows_events import NULL
import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import register,userlogin,createpoll,userdetails
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login,logout
from .models import *
from django.db import connection
import itertools
# Create your views here.
def index(request):
    return render(request,'index.html')

def regist(request):
    a=list(User.objects.values_list('username',flat=True))
    b=list(User.objects.values_list('email',flat=True))
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone_number=request.POST['phone_number']
        address=request.POST['address']
        gender=request.POST['gender']
        if request.FILES==True:
            dp=request.FILES['Your_profile_pic']
        else:
            dp=NULL
        c={'email':email,'first_name':first_name,'last_name':last_name,'phone_number':phone_number,'address':address,'gender':gender}
        
        if email in b:
            return render(request,'register.html',{'form':register,'user2':'block'})
        elif username in a:
            return render(request,'register.html',{'form':register(initial=c),'user1':'block'})
        else:
            user=User.objects.create_user(username,email,password)
            
            user.first_name=first_name
            user.last_name=last_name
            user_details=UserDetails(username=user,gender=gender,phone_number=phone_number,address=address,dp=dp)
            user.save()
            user_details.save()
            subject = 'Thanking for registering with us'
            message = 'Welcome to the Polls App'
            email_from = '190031710@kluniveristy.in'
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'register.html',{'success':'block','form':register})
    
    return render(request,'register.html',{'form':register})

def log(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        uname=list(User.objects.filter(email=email).values_list('username',flat=True))
        if len(uname)==0:
            return render(request,'login.html',{'form':userlogin,'status1':'block'})
        else:
            user = authenticate(request, username=uname[0], password=password)
            if user is not None:
                login(request,user)
                return redirect('/home/')
            else:
                return render(request,'login.html',{'form':userlogin,'status':'block'})
    return render(request,'login.html',{'form':userlogin})

def logout_view(request):
    logout(request)
    return render(request,'index.html')

@login_required
def home(request):
    user=request.user
    questions=PollQuestions.objects.exclude(username=user).values()
    dp=UserDetails.objects.get(username=user).dp.url
    
    if request.method=="POST":
        id=request.POST['poll_id']
        answer=request.POST['option']
        poll_id=PollQuestions.objects.get(poll_id=id)
        
        PollAnswer(poll_id=poll_id,user_id=user,answer=answer).save()
    return render(request,'home.html',{'polls':questions,'img':dp})


@login_required
def newpoll(request):
    username=request.user
    count=PollQuestions.objects.filter(username=username).count()
    
    if request.method=='POST':
        if count<=5:
            question=request.POST['question']
            opt1=request.POST['opt1']
            opt2=request.POST['opt2']
            opt3=request.POST['opt3']
            opt4=request.POST['opt4']
            
            PollQuestions(username=username,question=question,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4).save()
            return render(request,'newpoll.html',{'form':createpoll,'a':'created poll successfully'})
        else:
            return render(request,'newpoll.html',{'a':"Unable to create poll,limit upto 5 polls only"})
    
    print(request.user) 
    return render(request,'newpoll.html',{'form':createpoll})

@login_required
def mypolls(request):
    username=request.user
    details=list(User.objects.filter(username=username).values())[0]
    details1=list(UserDetails.objects.filter(username=username).values())[0]
    details.update(details1)
    form=userdetails(initial=details)
    polls=PollQuestions.objects.filter(username=username).values()
    
    #poll_ids=list(PollQuestions.objects.filter(username=username).values_list('poll_id',flat=True))
    answers=[]
    #for i in range(len(poll_ids)):
    #    answer=list(PollAnswer.objects.filter(poll_id=poll_ids[i]).values('user_id_id','answer'))
    #    answers.append(answer)
   
    
    
    
    

    return render(request,'mypolls.html',{'form':form,'polls':polls,'answers':answers})
