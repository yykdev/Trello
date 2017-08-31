from django import forms
from django.conf import settings

from dashboard.models import Board, Team


class BoardForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
    )

    class Meta:
        model = Board
        fields = (
            'title',
        )

    def save(self, **kwargs):
        author = kwargs.pop('author', None)
        team_id = kwargs.pop('team_id', None)
        team = Team.objects.get(pk=team_id)
        if not self.instance.pk or isinstance(author, settings.AUTH_USER_MODEL):
            self.instance.author = author
            self.instance.team = team
            super().save()
