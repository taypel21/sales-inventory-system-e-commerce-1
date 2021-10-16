from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import auth, messages
from .forms import UserForm, ProfileForm
from .mail_notifocations import MailNotificationForRegisteration
from e_commerce.settings import DEFAULT_FROM_EMAIL
from .decorators import *
from django.contrib.auth.decorators import login_required


# create user registration view
@authenticated_user
def user_registration(request):
    template_name = "accounts/register.html"
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        try:
            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect("accounts:user-registration")

                elif User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists')
                    return redirect("accounts:user-registration")

                else:
                    user = User.objects.create_user(
                        username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    Profile.objects.get_or_create(user=user)
                    messages.success(
                        request, f"account for {user.email} successfully created")

                    # initialize static data for mail notification
                    message_body = f"<h1>Hello {user.email}, your registration on bayshop is successful</h1>",
                    mail_subject = f"<h1>Registeration Successful</h1>"
                    sender_email = DEFAULT_FROM_EMAIL
                    recipient_email = user.email

                    send_notification = MailNotificationForRegisteration(
                        recipient_email, sender_email, mail_subject, message_body)

                    # send mail to user after registeration
                    send_notification.mail_new_customer()

                    # send mail to admin(s)
                    send_notification.mail_admin()

                    return redirect("accounts:user-login")
        except User.DoesNotExist:
            messages.error(request, "Password don't match!")
            return redirect("accounts:user-registration")
    else:
        return render(request, template_name)


# create user view login
@authenticated_user
def user_login(request):
    template_name = "accounts/login.html"
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return (request.POST.get('next'))
            messages.info(request, f'you are logged in as {username}')
            print('user logged')
            return redirect("product_list")
        else:
            messages.error(request, f'Invalid username or password')
            return redirect("accounts:user-login")
            # return render(request,'accounts/login.html',{'error':'Username or password is incorrect!'})

    else:
        return render(request, template_name, context={})


def logout(request):
    auth.logout(request)
    return redirect("product_list")


# User Profile Views
def userpage(request):
    user_form = UserForm(instance=request.user)
    profile_form=ProfileForm(instance=request.user)
    template_name = "accounts/user.html"
    context = {"user": request.user, "user_form": user_form, "profile_form":profile_form}
    return render(request, template_name, context)


@login_required
def updateprofile(request):
    template_name="accounts/user_profile.html"
    if request.method == 'POST':
        user_profile = Profile.objects.get(user=request.user)
        p_form = ProfileForm(request.POST,request.FILES,instance=user_profile)
        u_form = UserForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            user_profile = Profile.objects.get(user=request.user)
            messages.success(request,'Your Profile has been updated!')
            return redirect('accounts:userpage')
    else:
        p_form = ProfileForm(instance=request.user)
        u_form = UserForm(instance=request.user)

    context={'p_form': p_form, 'u_form': u_form}
    return render(request, 'accounts/user_profile.html',context )

