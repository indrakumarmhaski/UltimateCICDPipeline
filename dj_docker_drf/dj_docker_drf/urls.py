from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sample.urls')),  # Include the app's URLs
    # Add more URL patterns for other parts of your project
]
