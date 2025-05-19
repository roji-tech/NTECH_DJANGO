from django.shortcuts import render

from url_shorner.models import Url

# Create your views here.
def home(request):
    all_urls = Url.objects.all()

    if request.method == "POST":
        url = request.POST.get("url")
        if url:
            new_url = Url(url=url)
            new_url.save()
            all_urls = Url.objects.all()
    
    
    context = {
        "urls": all_urls,
    }
    return render(request, "url_shorner/index.html", context)