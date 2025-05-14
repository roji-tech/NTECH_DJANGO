from blog.views import about, home, create_blog
from django.urls import path

urlpatterns = [
    path('', home, name='index'),
    path('about/', about, name='about'),
    path('create/', create_blog, name='about'),
]
