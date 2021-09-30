from django.shortcuts import HttpResponse, render, redirect
from .models import *


def user_login(request):
    return HttpResponse("<h1>Welcome to your user account!</h1>")

def user_registration(request):
    pass


