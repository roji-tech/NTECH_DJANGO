from django.urls import path

from url_shorner.views import home, delete_url, redirect_to_url

app_name = "url_shorner"

urlpatterns = [
    path('', home, name='index'),
    path('<str:uid>/', redirect_to_url, name='redirect_to_url'),
    path('delete/<str:uid>/', delete_url, name='delete_url'),
]
