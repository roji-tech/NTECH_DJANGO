from django.shortcuts import render

from blog.forms import BlogForm
from .models import Blog
from django.contrib.auth import get_user_model

# User = settings.AUTH_USER_MODEL
User = get_user_model()

# Create your views here.


def home(request):
    form = BlogForm()

    if request.method == "POST":
        body = request.body
        print(body)
        print(request.POST)

        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()

    if request.method == "GET":
        ...
        print(dir(request))
        print(request.GET)
        print(request.path)

    context = {
        "myform": form
    }

    return render(request, "blog/index.html", context)


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
