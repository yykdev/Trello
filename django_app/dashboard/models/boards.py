from django.conf import settings
from django.db import models

from . import Team


class Board(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=50,
    )
    cover_img = models.ImageField(
        upload_to='contents/board/%Y%m%d',
        null=True,
        blank=True,
    )
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)