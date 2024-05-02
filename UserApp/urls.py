from django.urls import path
from . import views

urlpatterns = [

    path('login.html/', views.login, name='login'),
    path('logoutlogout.html/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile')
]
