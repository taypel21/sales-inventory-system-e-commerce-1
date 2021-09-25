from django.urls import path
from .views import *



urlpatterns = [
    path('register/', user_registeration, name="user-registeration")
]
