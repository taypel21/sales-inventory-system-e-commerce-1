from django.shortcuts import render, HttpResponse


def project_test_views(request):
    return HttpResponse("<h1>Welcome to sales inventory(e-commerce) landing page</h1>")
