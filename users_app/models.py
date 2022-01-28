from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
    # phone_number = models.CharField(max_length=20)
    # address = models.CharField(max_length=300)

    pass

    def __str__(self):
        return self.username

# def get_upload_path(instance, filename):
#     return f'images/avatars/{filename}'

# class User(AbstractUser):
#     avatar = models.ImageField(upload_to=get_upload_path, default='images/avatars/default_avatar.jpg')
#     phone_number = models.CharField(max_length=20)
#     address = models.CharField(max_length=300)

