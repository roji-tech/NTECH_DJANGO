from blog.views import about, delete_blog, edit_blog, home, create_blog, view_blog
from django.urls import path

app_name = "blog"

urlpatterns = [
    path('', home, name='index'),
    path('about/', about, name='about'),
    path('create/', create_blog, name='create_blog'),
    path('<blog_id>/', view_blog, name='view_blog'),
    path('edit/<blog_id>/', edit_blog, name='edit_blog'),
    path('delete/<blog_id>/', delete_blog, name='delete_blog'),
]
