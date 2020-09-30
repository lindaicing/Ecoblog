from django.contrib import admin
from django.urls import path
from .views import home, article, thanks

urlpatterns = [
    path('', home, name="home"),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>', article, name="article"),
    path('thanks', thanks, name="thanks")
]
