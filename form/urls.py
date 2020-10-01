from django.contrib import admin
from django.urls import path
from .views import formtest, contact, booker, pizza, shop

urlpatterns = [
    path('f', formtest, name="formtest"),
    path('contact', contact, name="contact"),


    path('booker', booker, name="booker"),
    path('pizza', pizza, name="pizza"),
    path('shop', shop, name="shop")
]
