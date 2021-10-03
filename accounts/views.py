from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth 
from django.contrib import messages
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
        if password1 ==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('accounts/register.html')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('accounts/register.html')
            else:    
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect("accounts:user-login")
        else:
            messages.info(request,"Password don't match!")
            return redirect('user-registration')
    else:
        return render(request,"accounts/register.html")
   
    
#create user view login

def user_login(request):
    template_name = "accounts/login.html"
    context = {}
    if (request.method == 'POST'):
        username=request.POST.get('username') 
        print(username)
        password=request.POST.get('password') 
        print(password)
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
      if(request.method == 'POST'):
        auth.logout(request)
        return redirect( "test_project")






# User Profile Views

# def userpage(request):
#     user_form= UserForm(instance=request.user)
#     #profile_form=ProfileForm(instance=request.user.profile)
#     return render(request=request, template_name="accounts/user.html", context={"user":request.user, "user_form":user_form})




