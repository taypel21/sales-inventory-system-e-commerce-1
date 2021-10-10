from django.urls import path
from .views import *


urlpatterns = [
    path('', product_list, name="product_list"),
    path('categories/<str:slug>/', category_list, name="category_list"),
    path('product/<str:slug>/', product_detail, name="product_detail"),
]
