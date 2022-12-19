from django.urls import path, include
from products import views

urlpatterns = [
   # url(r'^product/(?P<product_id>\w+)/', views.product, name='product'),
    path('product/<product_id>', views.product, name='product'),
   # path('product/<int:pk>', views.product, name='product'),

]
