from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from .form import LoginForm, SignupForm


def login(request):
    return django_login(
        request, authentication_form=LoginForm, template_name='member/log_in.html',
    )


def logout(request):
    return django_logout(request, template_name='index.html')


def signup(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'member/sign_up.html', context=context)


@login_required
def profile(request):
    return render(request, 'member/profile/profile.html')
