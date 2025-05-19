from django import forms

from url_shorner.models import Url


class UrlShortenerForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ['url']
        widgets = {
            'url': forms.TextInput(attrs={
                'placeholder': 'Enter URL here',
                'class': 'form-control'
            })
        }
        labels = {
            'url': 'Enter URL'
        }
        error_messages = {
            'url': {
                'required': 'This field is required.',
                'invalid': 'Please enter a valid URL.'
            }
        }
        help_texts = {
            'url': 'Please enter a valid URL.'
        }
