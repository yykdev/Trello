from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Member(AbstractUser):
    photo_profile = models.ImageField(upload_to='member/profile/%Y%m%d')
