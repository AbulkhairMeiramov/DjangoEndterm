from django.contrib import admin
from cart.models import Order, OrderItem, Transaction


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner']
    ordering = ['owner']
    search_fields = ['owner']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product']
    ordering = ['product']
    search_fields = ['product']







