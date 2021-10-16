from django.urls import path
from .views import *


urlpatterns = [
    path('', product_list, name="product_list"),
    path('categories/<slug:slug>/', category_list, name="category_list"),
    path('product/<slug:slug>/', product_detail, name="product_detail"),
    path('search item/', SearcItem.as_view(), name="search_item")
]
