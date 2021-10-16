from django.urls import path
from .views import cart_summary, add_to_cart


urlpatterns = [
    path('cart/', cart_summary, name="cart_summary"),
    path('add/', add_to_cart, name="add_to_cart"),
]
