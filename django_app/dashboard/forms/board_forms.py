from django import forms
from django.conf import settings

from dashboard.models import Board, Team, CardList


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
        title = self.cleaned_data['title']
        team = Team.objects.get(pk=team_id)
        board, created = Board.objects.get_or_create(
            author=author,
            team=team,
            title=title,
        )
        print(board, created)
        if created:
            CardList.objects.create(
                title='To-Do',
                board=board
            )
