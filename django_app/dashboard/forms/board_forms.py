from django import forms

from dashboard.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model=Board
        fields = (
            'author',
            'team',
            'title',
        )