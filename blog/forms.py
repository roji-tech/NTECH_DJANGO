from .models import Blog
from django import forms


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "user",
            "title",
            "content",
        ]

        widgets = {
            "user": forms.Select(attrs={"class": "form-control", "id": "user_idd"}),
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the title"}),
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your content here", "rows": 5}),
        }
