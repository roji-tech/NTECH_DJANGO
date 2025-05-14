from django.contrib import admin
from .models import Blog, Like, Comment

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    ...
    list_display = ["title", "id"]

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    ...
