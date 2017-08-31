from django.conf import settings
from django.db import models


class Team(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )
    title = models.CharField(
        max_length=50,
    )
    description = models.TextField()
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='shared_user',
        through='MembersTeams',
    )
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MembersTeams(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(auto_now_add=True)
