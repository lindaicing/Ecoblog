from django.contrib import admin
from form.models import Pizza, Beverage

class PizzaAdmin(admin.ModelAdmin):
    pass

class BeverageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Beverage, BeverageAdmin)
