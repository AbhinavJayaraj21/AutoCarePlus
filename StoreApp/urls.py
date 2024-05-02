from django.urls import path
from .import views

urlpatterns = [

    path('addstore/', views.addstore, name='add_store')
]