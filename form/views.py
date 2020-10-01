from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Pizza
from .forms import PizzaForm

# @csrf_exempt
# def my_view(request):
#     return HttpResponse('Hello world')

@csrf_exempt
def formtest(request):
    if request.method == "POST":
        print("post ",request.POST.get("pizzatopping"))
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
    


def booker(request):
    payload = "garden hose"
    return render(request, template_name="shop.html", context={"payload":payload})

@csrf_exempt
def pizza(request):
    form = "yea boi"
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            #newpizza = Pizza.objects.create(form.cleaned_data)
            #newpizza.save()
            #form.save()
        
            newpizza = Pizza(
                pizza_name = request.POST.get("pizza_name"),
                crust = request.POST.get("crust"),
                sauce = request.POST.get("sauce"),
                cheese = request.POST.get("cheese"),
                topping1 = request.POST.get("topping1"),
                topping2 = request.POST.get("topping2"),
                toasted = request.POST.get("toasted")
            )
            newpizza.save()
            return redirect("/thanks")  
    if request.method == "GET":
        form = PizzaForm()
    return render(request, template_name="pizza2.html", context={"form":form})

def shop(request):
    payload = "garden hose"
    return render(request, template_name="shop.html", context={"payload":payload})


# @csrf_exempt
# def pizza(request):
#     payload = "yea boi"
#     if request.method == "POST":
#         pizza_name = request.POST.get("pizza_name")
#         crust = request.POST.get("crust")
#         sauce = request.POST.get("sauce")
#         cheese = request.POST.get("cheese")
#         topping1 = request.POST.get("topping1")
#         topping2 = request.POST.get("topping2")
#         toasted = request.POST.get("toasted")
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
