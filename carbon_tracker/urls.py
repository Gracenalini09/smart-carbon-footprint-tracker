from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # /admin → Django admin
    path('', include('activityapp.urls')),    # /     → your home page
]
