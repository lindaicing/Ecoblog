from django.shortcuts import render
from .models import Post

def home(request):
    payload = Post.objects.all().order_by("-pub_date_time")
    return render(request, template_name="home.html", context={"payload":payload})

def article(request, year, month, day, slug):
    return render(request, template_name="article.html", context={
        "article":Post.objects.get(slug = slug),
    })

def contact(request):
    payload = [Post.objects.all().order_by("-pub_date_time")]
    return render(request, template_name="contact.html", context={"contact":payload})
