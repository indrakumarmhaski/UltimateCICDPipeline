from django.urls import path
from .views import HomeView

app_name = 'sample'  # This is optional but can help with namespacing URLs

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # Add more URL patterns for other views if needed
]
