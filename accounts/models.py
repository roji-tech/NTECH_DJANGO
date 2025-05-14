from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

# Create your models here.


class User(AbstractUser):
    ...
    
    def __str__(self) -> str:
        return f"{self.username} -- {self.email}"
    # role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="S")
