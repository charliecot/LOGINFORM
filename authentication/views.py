from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if len(pass1)>8 and len(pass1) <8:
            messages.error(request,'the password should be amost 8 characters')
        if not username.isalnum() :
               messages.error(request,'username should contain alphanumeric only')

        if pass1 == pass2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'the username exits')
                return redirect('signup')
                 

            else :
                user = User.objects.create_user(username=username, password=pass1, email=email)
                user.firstname=fname
                user.lastname=lname
                user.set_password(pass1)
                user.save()
                return redirect('signin')
        else:
            messages.error(request,'password does not match')
    return render(request,'signup.html')
    
def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['password1']

        user= authenticate(username=username,password=pass1)
       
        

        if user is not None:
            login(request, user)
            
    
            return render(request, 'index.html ')
            

        else:
            messages.error(request,'incorect username and password')
            return redirect('signin')    

        





    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('home')