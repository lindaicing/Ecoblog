from django.contrib import admin
from django.urls import path
from .views import home, article, contact

urlpatterns = [
    path('', home, name="home"),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>', article, name="article"),
    path('contact', contact, name="contact")
]
