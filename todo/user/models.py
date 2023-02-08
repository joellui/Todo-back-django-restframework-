from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)