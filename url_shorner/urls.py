from django.urls import path

from url_shorner.views import home

app_name = "url_shorner"

urlpatterns = [
    path('', home, name='index'),
]
