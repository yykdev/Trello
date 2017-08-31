from django import forms
from django.conf import settings

from dashboard.models import Team


class TeamsForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
    )
    description = forms.Textarea()

    class Meta:
        model = Team
        fields = (
            'title',
            'description',
        )

    def save(self, **kwargs):
        author = kwargs.pop('author', None)
        if not self.instance.pk or isinstance(author, settings.AUTH_USER_MODEL):
            self.instance.author = author
            super().save()
