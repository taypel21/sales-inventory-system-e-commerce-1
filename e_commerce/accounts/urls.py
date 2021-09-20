from django.urls import path
from .views import user_account_views


urlpatterns = [
    path('users/', user_account_views, name="users")
]
