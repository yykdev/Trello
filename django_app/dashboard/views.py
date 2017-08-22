from django.shortcuts import render

# Create your views here.
from .models import Team
from .forms.team_forms import TeamsForm


def team_list(request):
    teams = Team.objects.filter(author=request.user)
    context = {
        'teams': teams,
    }
    return render(request, '', context=context)


def team_make(request):
    if request.method == 'POST':
        forms = TeamsForm(request.data)
        if forms.is_valid():
            forms.save(commit=False)
            forms.author=request.user
            forms.save()
    else:
        forms = TeamsForm()
    context = {
        'forms': forms
    }
    return render(request, '', context=context)