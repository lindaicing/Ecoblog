from django.db import models
from django.forms import ModelForm

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=500,
                    # label = "Pizza Name",
                    # initial = "What is your name?",
                    help_text = "Type your name in here"
                    )
    crust = models.CharField(max_length=100,
                    # label = "Crust",
                    # initial = "Thick Crust",
                    help_text = "Please choose your crust preference"
                    )
    
    sauce = models.CharField(max_length=100)
    cheese = models.CharField(max_length=100)
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100, blank=True, default="")

    toasted = models.BooleanField(null=True)

    def __str__(self):
        return f'Pizza Name: {self.pizza_name}'

class PizzaForm(ModelForm): #if a field is removed here but not in model, the field will still show in admin
    class Meta:
        model = Pizza
        # fields = ['pizza_name', 'crust', 'sauce', 'cheese',
        #  "topping1", "topping2", "toasted"]
        exclude = ['']
        labels = {'pizza_name':'Pizza Name', 
                    'crust': 'Crust',
                }

class Beverage(models.Model):
    drink_name = models.CharField(max_length=500, help_text="What drink would you like?")
    drink_size = models.CharField(max_length=500, help_text="What size?")

    def __str__(self):
        return f'Drink: {self.drink_name}'

class BeverageForm(ModelForm):
    class Meta:
        model = Beverage
        exclude = []
        labels = {
            'drink_name':'Drink Name',
            'drink_size':'Size',
        }
