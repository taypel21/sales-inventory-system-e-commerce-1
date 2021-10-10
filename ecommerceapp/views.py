from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import *


def category_list(request, slug):
    categories = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=categories)
    template_name = "base.html"
    context = {"categories": categories, "products": products}
    return render(request, template_name, context)


def product_list(request):
    template_name = "ecommerceapp/product_list.html"
    products = Product.objects.filter(available=True)
    context = {"products": products}
    return render(request, template_name, context)


@login_required(login_url="accounts:user-login", redirect_field_name="next")
def product_detail(request, slug):
    template_name = "ecommerceapp/product_detail.html"
    product = get_object_or_404(Product, slug=slug)
    context = {"product": product}
    return render(request, template_name, context)
