from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput,
        required=True,
    )
    email = forms.EmailField(
        widget=forms.EmailInput,
        required=True,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username already exist'
            )
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'Password missmatch'
            )
        return password2

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password2']
        return User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
