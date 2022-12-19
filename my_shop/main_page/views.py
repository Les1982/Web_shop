from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *



def main_page(request):
    form = SubscriberForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
       # data = form.cleaned_data
       # print(data["name"])
        new_form = form.save()

    return render(request, 'main_page\main_page.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    products_images_cameras = ProductImage.objects.filter(product__category__name='camera', is_active=True, is_main=True)
    products_images_laptops = ProductImage.objects.filter(product__category__name='laptop', is_active=True, is_main=True)
    return render(request, 'main_page\home.html', locals())