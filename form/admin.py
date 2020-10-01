from django.contrib import admin
from form.models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pizza, PizzaAdmin)
