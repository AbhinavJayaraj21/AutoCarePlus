
from django.urls import path
from AdminApp import views

urlpatterns = [

    path('', views.home, name='home'),
    path('product/<int:id>', views.view, name='view'),
    path('pproduct/<int:id>',views.part_view, name='pview')
]
