from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *

app_name = "accounts"

urlpatterns = [
    path('register/', user_registration, name="user-registration"),
    path('login/', user_login, name="user-login"),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            subject_template_name='accounts/password_reset_subject.txt',
            email_template_name='accounts/password_reset_email.html',
            success_url='password_reset_done'
        ),
        name='password_reset'
    ),
    path(
        'password-reset/password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
    path("user/", userpage, name="userpage"),
    path("logout/", logout, name="logout"),

]
