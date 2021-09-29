from django.shortcuts import HttpResponse, render



def user_registeration(request):
      template_name = "accounts/register.html"
      context = {}
      return render(request, template_name)


def user_login(request):
      template_name = "accounts/index.html"
      context = {}
      return render(request, template_name)