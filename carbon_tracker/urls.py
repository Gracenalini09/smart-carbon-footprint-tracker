from django.contrib import admin 
from django.urls import path, include
from django.contrib.auth import views as auth_views
from activityapp import views as app_views   # 👈 add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('activityapp.urls')),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', app_views.logout_view, name='logout'),  # 👈 use our view
]
