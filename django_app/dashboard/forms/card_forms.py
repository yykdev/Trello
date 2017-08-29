from django import forms

from dashboard.models.cards import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = (
            'title',
            'description',
            'cardlist',
        )