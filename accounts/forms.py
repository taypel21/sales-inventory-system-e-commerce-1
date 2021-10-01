from .models import Profile
from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User=get_user_model()



class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
        attrs={
        "class": "form-control",
        "label":"username",
        "placeholder": "Enter your username"
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "label":"password",
                "id": "user-password",
                "placeholder": "Enter password"
            }
        )
    )


class RegisterForm(forms.ModelForm):
    
    class Meta:
        model= User
        fields= ('username', 'email', 'password', 'password2')


    username = forms.CharField(
        widget=forms.TextInput(
        attrs={
        "class": "form-control",
        "label":"username",
        "placeholder": "Enter your username"
    }))


    
    email = forms.EmailField(
        widget=forms.TextInput(
        attrs={
        "class": "form-control",
        "label":"Email",
        "placeholder": "Enter your Email"
    }))

    
    password = forms.CharField(
         widget=forms.PasswordInput(
             attrs={
                  "class": "form-control",
                 "id": "user-password",
              "placeholder": "Enter password"
            }
         )
     )
    password2 = forms.CharField(
        
         widget=forms.PasswordInput(
             attrs={
                    "class": "form-control",
                    "id": "user-confirm-password",
                    "placeholder": "Confirm password"
              }
          )
      )

  
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email')



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('user','address','city','state', 'phone_no')
