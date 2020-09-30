from django.shortcuts import render
from .models import Post
from django.views.decorators.csrf import csrf_exempt

def home(request):
    payload = Post.objects.all().order_by("-pub_date_time")
    return render(request, template_name="home.html", context={"payload":payload})

def article(request, year, month, day, slug):
    return render(request, template_name="article.html", context={
        "article":Post.objects.get(slug = slug),
    })

@csrf_exempt
def thanks(request):
    payload = [Post.objects.all().order_by("-pub_date_time")]
    return render(request, template_name="thanks.html", context={"contact":payload})
