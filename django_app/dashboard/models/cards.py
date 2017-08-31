from django.db import models

from dashboard.models import Board
from . import CardList


class Card(models.Model):
    title = models.CharField(
        max_length=20,
    )
    description = models.TextField()

    board = models.ForeignKey(
        Board,
    )

    cardlist = models.ForeignKey(
        CardList,
    )