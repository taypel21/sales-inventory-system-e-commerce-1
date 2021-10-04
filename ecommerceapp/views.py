from django.shortcuts import render




def project_test_views(request):
    return render(request,'ecommerceapp/home.html')
