from django.contrib import admin
from django.urls import path
from .views import formtest, contact

urlpatterns = [
    path('f', formtest, name="formtest"),
    path('contact', contact, name="contact"),
]
