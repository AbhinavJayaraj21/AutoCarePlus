
from django.urls import path
from . import views

urlpatterns = [

    path('acessory', views.accessory, name='acessory'),
    path('buyaccessory/<int:id>', views.buy_accessory, name='abuy')
]