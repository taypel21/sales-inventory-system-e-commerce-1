from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth 
from django.contrib import messages
from .forms import UserForm
#create user registration view

def user_registration(request):
    template_name = "accounts/register.html"
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        try:
            if password1 ==password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                    return render (request,'accounts/register.html', {'error': 'Email is already taken!'})
                elif User.objects.filter(username=username).exists():
                    messages.error(request,'Username already exists')
                    return render (request,'accounts/register.html', {'error': 'Username is already exists!'})
                else:    
                    user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    print('User Account Created')
                    return redirect("accounts:user-login")

        except User.check_password:
            messages.error(request,"Password don't match!")
            return render(request,'accounts/register.html', {'error': 'Passwords do not match'})
    else:
        return render(request,"accounts/register.html")
   
    
#create user view login

def user_login(request):
    template_name = "accounts/login.html"
    context = {}
    if (request.method == 'POST'):
        username=request.POST.get('username') 
        password=request.POST.get('password') 
        user= auth.authenticate(username=username,password=password)
       
        if user is not None :
            auth.login(request,user)
            print('user logged')
            return redirect("test_project")  
        else:
            return render(request,'accounts/login.html',{'error':'Username or password is incorrect!'})     
    
    else:
       return render(request,'accounts/login.html',context={})  
            


def logout (request):
        auth.logout(request)
        return redirect( "test_project")






# User Profile Views

def userpage(request):
    user_form= UserForm(instance=request.user)
    #profile_form=ProfileForm(instance=request.user.profile)
    return render(request=request, template_name="accounts/user.html", context={"user":request.user, "user_form":user_form})




