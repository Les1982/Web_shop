from django.urls import path, include
from . import views

urlpatterns  =[
 #   path('', views.home, name='home'),
    path('basket_adding/', views.basket_adding, name='basket_adding'),
    path('checkout/', views.checkout, name='checkout'),
    ]