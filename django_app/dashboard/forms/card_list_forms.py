from django import forms

from dashboard.models import CardList


class CardListForm(forms.ModelForm):
    class Meta:
        model = CardList
        fields = (
            'title',
            'board',
        )
