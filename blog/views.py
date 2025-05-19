from django.shortcuts import render, redirect

from blog.forms import BlogForm
from .models import Blog
from django.contrib.auth import get_user_model

# User = settings.AUTH_USER_MODEL
User = get_user_model()

# Create your views here.


def home(request):
    user = User.objects.get(id=1)
    # print("\n\n", "Result: ", user, user.email, user.username, user.password, "\n\n")

    # print(Blog.objects.create(user=user, title="New Blog",
    #       content="this is a new blog",))

    blogs = Blog.objects.all()

    context = {
        "blogs": blogs,
        "user": user,
    }
    return render(request, "blog/index.html", context)


def create_blog(request):
    form = BlogForm()

    if request.method == "POST":
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:index")

    if request.method == "GET":
        ...
        print(dir(request))
        print(request.GET)
        print(request.path)

    context = {
        "myform": form
    }

    return render(request, "blog/create.html", context)


def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    form = BlogForm()

    print(blog.id, blog.content)
    print(blog.title)

    form = BlogForm(instance=blog)

    if request.method == "POST":
        form = BlogForm(data=request.POST, instance=blog)
        if form.is_valid():
            form.save()
        return redirect("index")

    if request.method == "GET":
        ...
        print(dir(request))
        print(request.GET)
        print(request.path)

    context = {
        "myform": form
    }

    return render(request, "blog/index.html", context)


def view_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {}

    if request.method == "GET":
        context = {
            "blog": blog
        }

    return render(request, "blog/details.html", context)


def about(request):
    return render(request, "blog/about.html")


def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        blog.delete()
        return redirect("blog:index")
    context = {
        "blog": blog
    }
    return render(request, "blog/delete.html", context)
