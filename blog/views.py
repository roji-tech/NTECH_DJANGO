from django.shortcuts import render
from .models import Blog
from django.contrib.auth import get_user_model

# User = settings.AUTH_USER_MODEL
User = get_user_model()

# Create your views here.


def home(request):
    return render(request, "blog/index.html")


def create_blog(request):
    user = User.objects.get(id=1)
    # print("\n\n", "Result: ", user, user.email, user.username, user.password, "\n\n")

    # print(Blog.objects.create(user=user, title="New Blog",
    #       content="this is a new blog",))

    blogs = Blog.objects.all()

    context = {
        "blogs": blogs
    }
    return render(request, "blog/index.html", context)


def about(request):
    return render(request, "blog/about.html")
