from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import *


def categories(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return context


def product_list(request):
    template_name = "ecommerceapp/product_list.html"
    products = Product.objects.filter(available=True)
    context = {"products": products}
    return render(request, template_name, context)


def product_detail(request, slug):
    template_name = "ecommerceapp/product_detail.html"
    product = get_object_or_404(Product, slug=slug)
    context = {"product": product}
    return render(request, template_name, context)


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    template_name = "ecommerceapp/list_by_category.html"
    context = {"category": category, "products": products}
    return render(request, template_name, context)
