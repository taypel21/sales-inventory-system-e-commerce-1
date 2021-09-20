from django.shortcuts import render, HttpResponse


def user_account_views(request):
    return HttpResponse("<h1>Welcome to user accounts</h1>")
