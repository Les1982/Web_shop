from django.contrib import admin
from .models import *
from django.contrib.admin.options import TabularInline

class ProductInOrderInline(TabularInline):
    model = ProductInOrder
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order
# Register your models here.
admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]


    class Meta:
        model = ProductInOrder
# Register your models here.
admin.site.register(ProductInOrder, ProductInOrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status
# Register your models here.
admin.site.register(Status, StatusAdmin)


class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]


    class Meta:
        model = ProductInBasket
# Register your models here.
admin.site.register(ProductInBasket, ProductInBasketAdmin)