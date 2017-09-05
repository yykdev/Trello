from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from .form import LoginForm, SignupForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            django_login(request, user)
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('index')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'member/log_in.html', context=context)


def logout(request):
    django_logout(request)
    return redirect('index')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
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
