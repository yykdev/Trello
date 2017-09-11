from django import forms

from dashboard.models import CardList, Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = (
            'title',
            'description',
            'cardlist',
        )

    def save(self, **kwargs):
        cardlist_id = kwargs.get('cardlist_id', None)
        cardlist = CardList.objects.get(pk=cardlist_id)
        self.instance.cardlist = cardlist
        super().save(**kwargs)
