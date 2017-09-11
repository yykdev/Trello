from django import forms

from dashboard.models import CardList, Board


class CardListForm(forms.ModelForm):
    class Meta:
        model = CardList
        fields = (
            'title',
        )

    def save(self, **kwargs):
        board_id = kwargs.pop('board_id', None)
        board = Board.objects.get(pk=board_id)
        self.instance.board = board
        super().save(**kwargs)
