from django.shortcuts import redirect, render

from url_shorner.forms import UrlShortenerForm
from url_shorner.models import Url

# Create your views here.


def home(request):
    all_urls = Url.objects.all()
    form = UrlShortenerForm()

    context = {
        "urls": all_urls,
        "myform": form,
    }

    if request.method == "POST":
        form = UrlShortenerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "url_shorner/index.html", context)

    return render(request, "url_shorner/index.html", context)


def delete_url(request, uid):
    url = Url.objects.get(uid=uid)
    url.delete()
    return redirect("url_shorner:index")
