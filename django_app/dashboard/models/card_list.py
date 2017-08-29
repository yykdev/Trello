from django.db import models

from . import Board


class CardList(models.Model):
    title = models.CharField(max_length=30)

    board = models.ForeignKey(
        Board,
    )