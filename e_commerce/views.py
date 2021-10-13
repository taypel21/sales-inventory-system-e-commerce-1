from django.shortcuts import render, HttpResponse



def home_page(request):
      template_name = "base.html"
      return render(request, template_name)
