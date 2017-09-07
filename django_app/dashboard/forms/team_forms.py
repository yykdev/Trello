from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model

from dashboard.models import Team

Member = get_user_model()


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
        if not self.instance.pk or isinstance(author, Member):
            self.instance.author = author
        super().save(**kwargs)
