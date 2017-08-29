from django.shortcuts import render, redirect

# Create your views here.
from dashboard.forms import BoardForm, CardListForm, CardForm
from dashboard.models import Board, CardList
from dashboard.models.cards import Card
from .models import Team
from .forms.team_forms import TeamsForm


def team_dashboard(request):
    if request.method == 'POST':
        form = TeamsForm(data=request.POST)
        if form.is_valid():
            form.save(author=request.user)
    else:
        form = TeamsForm()
    teams = Team.objects.filter(author=request.user)
    context = {
        'teams': teams,
        'form': form,
    }
    return render(request, 'contents/team_dashboard.html', context=context)


def team_make(request):
    if request.method == 'POST':
        forms = TeamsForm(request.data)
        if forms.is_valid():
            forms.save(commit=False)
            forms.author = request.user
            forms.save()
    else:
        forms = TeamsForm()
    context = {
        'forms': forms
    }
    return render(request, '', context=context)


def board_make(request, team_id):
    if request.method == 'POST':
        forms = BoardForm(request.data)
        if forms.is_valid():
            team = Team.objects.get(pk=team_id)
            forms.save(commit=False)
            forms.author = request.user
            forms.team = team
            forms.save()
    else:
        forms = BoardForm()
    context = {
        'forms': forms
    }
    return render(request, '', context=context)


def card_dashboard(request, board_id):
    board = Board.objcets.get(pk=board_id)
    cardlists = CardList.objects.filter(board=board)
    context = {
        'board_title': board.title,
        'team_title': board.team.title,
        'board_id': board_id,
        'cardlists': cardlists,
    }
    return render(request, '', context=context)


def card_list_make(request, board_id):
    if request.method == 'POST':
        forms = CardListForm(request.data)
        if forms.is_valid():
            board = Board.objects.get(pk=board_id)
            forms.save(commit=False)
            forms.board = board
            forms.save()
    else:
        forms = CardListForm()
    context = {
        'forms': forms,
    }
    render(request, '', context=context)


def card_make(request, cardlist_id):
    if request.method == 'POST':
        forms = CardForm(request.data)
        if forms.is_valid():
            cardlist = CardList.objects.get(pk=cardlist_id)
            forms.save(commit=False)
            forms.cardlist=cardlist_id
            forms.save()
    else:
        forms = CardForm()
    context = {
        'forms': forms,
    }
    return render(request, '', context=context)


def update_card_position(request, board_id):
    if request.method == 'POST':
        # 카드별 카드리스트 id 값 업데이트
        cards = eval(request.body.decode("utf-8"))
        list_id = cards['list_id']
        positions = cards['positions'].split(';')
        if positions[0] != '':
            card_list = Card.objects.filter(pk__in=positions)
            card_list.update(cardlist=list_id)
        return redirect('contents:dashboard_card', board_id=board_id)
    else:
        return redirect('contents:dashboard_card', board_id=board_id)
