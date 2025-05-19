from django.db import models
from uuid import uuid4

# Create your models here.


class Url(models.Model):
    url = models.URLField()
    uid = models.CharField(max_length=5, unique=True,
                           primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uid} - {self.url}"
