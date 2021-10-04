from django.shortcuts import render, redirect
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
            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                    return redirect("accounts:user-registration")
                    #return render(request,'accounts/register.html', {'error': 'Email is already taken!'})
                elif User.objects.filter(username=username).exists():
                    messages.error(request,'Username already exists')
                    return redirect("accounts:user-registration")
                    #return render (request,'accounts/register.html', {'error': 'Username is already exists!'})
                else:    
                    user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    print('User Account Created')
                    return redirect("accounts:user-login")

        except User.DoesNotExist:
            messages.error(request,"Password don't match!")
            return redirect("accounts:user-registration")
            #return render(request,'accounts/register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, template_name)
   
    
#create user view login
def user_login(request):
    template_name = "accounts/login.html"
    if (request.method == 'POST'):
        username=request.POST.get('username') 
        password=request.POST.get('password') 
        user= auth.authenticate(username=username, password=password)
       
        if user is not None :
            auth.login(request,user)
            messages.info(request, f'you are logged in as {username}')
            print('user logged')
            return redirect("test_project")  
        else:
            messages.error(request, f'Invalid username or password')
            return redirect("accounts:user-login")
            #return render(request,'accounts/login.html',{'error':'Username or password is incorrect!'})     
    
    else:
       return render(request, template_name, context={})  
            

def logout (request):
    auth.logout(request)
    return redirect( "test_project")


# User Profile Views
def userpage(request):
    user_form= UserForm(instance=request.user)
    template_name="accounts/user.html"
    context={"user":request.user, "user_form":user_form}
    return render(request, template_name, context)
