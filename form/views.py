from django.shortcuts import render
# from .models import Post
from django.views.decorators.csrf import csrf_exempt

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
    
# checkbox, radio btn, etc.
