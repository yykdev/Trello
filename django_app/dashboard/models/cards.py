from django.db import models

from . import CardList


class Card(models.Model):
    title = models.CharField(
        max_length=20,
    )
    description = models.TextField()

    cardlist = models.ForeignKey(
        CardList,
    )