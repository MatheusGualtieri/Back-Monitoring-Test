from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=250, null=False)
    email = models.EmailField(unique=True, null=False)
