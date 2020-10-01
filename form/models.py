from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=500)
    crust = models.CharField(max_length=100)
    
    sauce = models.CharField(max_length=100)
    cheese = models.CharField(max_length=100)
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100, blank=True, default="")

    toasted = models.BooleanField(null=True)

    def __str__(self):
        return f'Post Title: {self.pizza_name}'
