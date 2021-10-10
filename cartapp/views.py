from django.shortcuts import render


def cart_view(request):
    template_name = 'cart/cart_list.html'
    context = {}
    return render(request, template_name, context)
