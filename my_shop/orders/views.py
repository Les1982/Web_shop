from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .forms import ChekoutContactForm
from orders.models import *
from django.contrib.auth.models import User


# Create your views here.
def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id");
    nmb = data.get("nmb")

    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, is_active=True, defaults={"nmb": nmb})
    if not created:
        new_product.nmb += int(nmb)
        new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] =item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)


    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    #if not session_key:
    #    request.session.cycle_key()
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form = ChekoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print("yes")
            data = request.POST
            name = data["name"]
            phone = data["phone"]
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name":name })

            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=2 )
            print("################# ",order,data.items())

            for name, value in data.items():
                print( data["name"])
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    product_in_basket.nmb = value
                    product_in_basket.order = order
                    print("Cycle: ", product_in_basket.order)
                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_basket.product, nmb=product_in_basket.nmb,
                                                   price_per_item=product_in_basket.price_per_item,
                                                   total_price=product_in_basket.total_price,
                                                   order=product_in_basket.order)
        else:
            print("no")


    return render(request, 'orders/checkout.html', locals())