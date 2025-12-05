from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('activity/add/', views.add_activity, name='add_activity'),
    path('activity/list/', views.activity_list, name='activity_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
