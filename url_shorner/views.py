from django.shortcuts import get_object_or_404, redirect, render

from url_shorner.forms import UrlShortenerForm
from url_shorner.models import Url
from django.contrib import messages

# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    from django.db.models import Value
    all_urls = Url.objects.all()
    # .annotate(
    #     short_url=Value(f"{request.build_absolute_uri('/shortner/uid/')}",
    # )
    messages.success(request, 'This is a success message.')
    messages.error(request, 'An error occurred.')
    messages.warning(request, 'This is a warning.')
    messages.info(request, 'Just an informational message.')
    form = UrlShortenerForm()

    context = {
        "urls": all_urls,
        "myform": form,
    }

    if request.method == "POST":
        form = UrlShortenerForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Item created.')
            return render(request, "url_shorner/index.html", context)

    return render(request, "url_shorner/index.html", context)


def delete_url(request, uid):
    url = Url.objects.get(uid=uid)
    url.delete()
    return redirect("url_shorner:index")


def redirect_to_url(request, uid):
    # url = Url.objects.get(uid=uid)
    url = get_object_or_404(Url, uid=uid)
    # Redirect to a specific URL

    return redirect(url.url)
