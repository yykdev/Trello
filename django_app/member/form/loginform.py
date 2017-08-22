from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': '이메일을 입력하세요.',
            }
        )
    )

    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 입력하세요.'
            }
        )
    )
