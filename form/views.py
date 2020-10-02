from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt #This ignores the token, but if you add the token to the form then you don't need to NOT include the csrf
from .models import Pizza, Beverage
from .models import PizzaForm, BeverageForm

# @csrf_exempt
# def my_view(request):
#     return HttpResponse('Hello world')

@csrf_exempt
def formtest(request):
    if request.method == "POST":
        print("post ",form.cleaned_data("pizzatopping"))
        method = request.method
        message = "we used POST"
    if request.method == "GET":
        print("get ",request.GET.get("formmessage")) # in quotes, getting variable name from HTML template
        method = request.method
        message = "we used GET!!!"
    payload = "wheee"
    return render(request, template_name="formtest.html", context={"method": method, "message": message})

@csrf_exempt
def contact(request):
    payload = "Yeehaw"
    return render(request, template_name="contact.html", context={"contact":payload})

def pizza(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():

            """
            newpizza = Pizza(
                pizza_name = form.cleaned_data["pizza_name"],
                crust = form.cleaned_data["crust"],
                sauce = form.cleaned_data["sauce"],
                cheese = form.cleaned_data["cheese"],
                topping1 = form.cleaned_data["topping1"],
                topping2 = form.cleaned_data["topping2"],
                toasted = form.cleaned_data["toasted"]
            )
            newpizza.save()"""
            form.save()
            return redirect(request, "/thanks")  
    if request.method == "GET":
        form = PizzaForm(
            initial = {'pizza_name': 'George'}
        )
    return render(request, template_name="pizza2.html", context={"form":form})

@csrf_exempt
def beverage(request):
    if request.method=="POST":
        form = BeverageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/thanks")
    if request.method=="GET":
        form = BeverageForm()
    # payload = "garden hose"
    return render(request, template_name="beverage.html", context={"form":form})




def orders(request):
    open_orders = Pizza.obects.all()
    return render(request, template_name="orders.html", context={"open_orders":open_orders})

from django.views.generic import ListView

class OrdersView(ListView):
    model=Pizza
    template_name = "orders.html"
    context_object_name = 'open_orders'

# @csrf_exempt
# def pizza(request):
#     payload = "yea boi"
#     if request.method == "POST":
#         pizza_name = form.cleaned_data("pizza_name")
#         crust = form.cleaned_data("crust")
#         sauce = form.cleaned_data("sauce")
#         cheese = form.cleaned_data("cheese")
#         topping1 = form.cleaned_data("topping1")
#         topping2 = form.cleaned_data("topping2")
#         toasted = form.cleaned_data("toasted")
#         print(pizza_name, crust, sauce)
#         newpizza = Pizza(
#             pizza_name = pizza_name,
#             crust = crust,
#             sauce = sauce,
#             cheese = cheese,
#             topping1 = topping1,
#             topping2 = topping2,
#             toasted = toasted
#         )
#         newpizza.save()
#         return redirect("/thanks")
#     if request.method == "GET":
#         payload = "nada"
#     return render(request, template_name="pizza.html", context={"payload":payload})
