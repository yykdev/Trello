from django import forms

from dashboard.models import CardList, Card, Board


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = (
            'title',
            'description',
        )

    def save(self, **kwargs):
        cardlist_id = kwargs.pop('cardlist_id', None)
        title = self.cleaned_data['title']
        description = self.cleaned_data['description']
        cardlist = CardList.objects.get(pk=cardlist_id)
        Card.objects.create(
            title=title,
            description=description,
            cardlist=cardlist,
            board=cardlist.board,
        )
        return cardlist.board.id