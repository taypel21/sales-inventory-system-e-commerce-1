from django.shortcuts import render



def user_registration(request):
    template_name = "accounts/register.html"
    context = {}
    return render(request, template_name)


def user_login(request):
    template_name = "accounts/login.html"
    context = {}
    return render(request, template_name)
