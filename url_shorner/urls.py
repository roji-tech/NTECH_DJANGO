from django.urls import path

from url_shorner.views import home, delete_url

app_name = "url_shorner"

urlpatterns = [
    path('', home, name='index'),
    path('delete/<uid>/', delete_url, name='delete_url'),
]
