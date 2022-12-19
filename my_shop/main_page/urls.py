from django.urls import path, include
from . import views

urlpatterns  =[
    path('', views.home, name='home'),
    path('main_page/', views.main_page, name='main_page'),
]

