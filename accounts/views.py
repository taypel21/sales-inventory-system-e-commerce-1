from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django import forms
from django.contrib import messages
from .forms import LoginForm,RegisterForm, UserForm, ProfileForm
User= get_user_model()


#create user registration view

def user_registration(request):
    template_name = "accounts/register.html"
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('accounts:user-login')
            #return HttpResponseRedirect('login')
            
        
    return render(request, 'accounts/register.html', {"form": form})

    

#create user view login form

def user_login(request):
    template_name = "accounts/login.html"
    context = {}
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(
                username= form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password"),
            )
            
            if user is not  None:
                #request.user==user
                login(request,user)
                return redirect('test_project')
        
            
    message = 'Login failed!'      
            
    return render(request,'accounts/login.html', {"form": form, 'message': message})


def logout_view(request):
      logout(request)
      #return render(request,'accounts/logout.html')
      return HttpResponseRedirect( "test_project")


# User Profile Views

def userpage(request):
    user_form= UserForm(instance=request.user)
    #profile_form=ProfileForm(instance=request.user.profile)
    return render(request=request, template_name="accounts/user.html", context={"user":request.user, "user_form":user_form})




