from django import forms
    
class PizzaForm(forms.Form):
    CHOICES = [(True, 'Yes'), (False, "no")]
    pizza_name = forms.CharField(max_length=500,
                    label = "Pizza Name",
                    initial = "What is your name?",
                    help_text = "Type your name in here"
    )
    crust = forms.CharField(max_length=100,
                    label = "Crust",
                    initial = "Thick Crust",
                    help_text = "Please choose your crust preference"
    )
    sauce = forms.CharField(max_length=100)
    cheese = forms.CharField(max_length=100)
    topping1 = forms.CharField(max_length=100,
                    label = "First Topping",
                    initial = "Green Eggs",
                    help_text = "Choose a first topping"
    )
    topping2 = forms.CharField(max_length=100,
                    label = "Second Topping",
                    initial = "Ham",
                    help_text = "Choose a second topping"
    )
    toasted = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    #bubba = forms.CharField(widget=forms.Textarea)
