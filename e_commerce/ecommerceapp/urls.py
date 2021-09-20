from django.urls import path
from .views import project_test_views


urlpatterns = [
    path('', project_test_views, name="test_project")
]
