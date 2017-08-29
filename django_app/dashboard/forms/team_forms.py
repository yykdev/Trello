from django import forms

from dashboard.models import Team


class TeamsForm(forms.ModelForm):
    # author = forms.CharField(
    #     required=True
    # )
    title = forms.CharField(
        required=True
    )
    description = forms.Textarea()
    # members = forms.CharField(
    #     required=False
    # )

    class Meta:
        model = Team
        fields = (
            'author',
            'title',
            'description',
        )
