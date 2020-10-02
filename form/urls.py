from django.contrib import admin
from django.urls import path
from .views import formtest, contact, pizza, beverage, OrdersView

urlpatterns = [
    path('f', formtest, name="formtest"),
    path('contact', contact, name="contact"),


    path('pizza', pizza, name="pizza"),
    path('beverage', beverage, name="beverage"),
    path('orders', OrdersView.as_view(), name="orders")
]
