from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string

from dashboard.forms import BoardForm, CardListForm, CardForm
from dashboard.models import Board, CardList
from dashboard.models.cards import Card
from .models import Team
from .forms.team_forms import TeamsForm


@login_required
def team_dashboard(request):
    teams = Team.objects.filter(author=request.user)
    context = {
        'teams': teams,
        'search_on': True,
    }
    return render(request, 'contents/team_dashboard.html', context=context)


# 팀생성 모달 렌더링 함수
def team_create_modal(request):
    data = {}
    if request.method == 'POST':
        form = TeamsForm(data=request.POST)
        if form.is_valid():
            form.save(author=request.user)
            data['form_is_valid'] = True
            teams = Team.objects.filter(author=request.user)
            context = {
                'teams': teams,
            }
            data['html_team_list'] = render_to_string(
                'contents/partial/partial_team_list.html',
                context=context,
                request=request,
            )
        else:
            data['form_is_valid'] = False
    else:
        form = TeamsForm()
    context = {
        'form': form,
    }
    data['html_form'] = render_to_string(
        'contents/modal/team_modal.html',
        context=context,
        request=request,
    )
    return JsonResponse(data)


def team_modify_modal(request, team_id):
    data = {}
    team = Team.objects.get(pk=team_id)
    if request.method == 'POST':
        form = TeamsForm(data=request.POST, files=request.FILES, instance=team)
        form.save(author=request.user)
        data['form_is_valid'] = True
        teams = Team.objects.filter(author=request.user)
        context = {
            'team_id': team_id,
            'teams': teams,
        }
        data['html_team_list'] = render_to_string(
            'contents/partial/partial_team_list.html',
            context=context,
            request=request,
        )
    else:
        form = TeamsForm(instance=team)
    context = {
        'team_id': team_id,
        'form': form,
    }
    data['html_form'] = render_to_string(
        'contents/modal/team_modal.html',
        context=context,
        request=request,
    )
    return JsonResponse(data)


@login_required
def board_make(request, team_id):
    data = {}
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save(author=request.user, team_id=team_id)
            data['form_is_valid'] = True
            teams = Team.objects.filter(author=request.user)
            context = {
                'teams': teams,
            }
            data['html_team_list'] = render_to_string(
                'contents/partial/partial_team_list.html',
                context=context,
                request=request,
            )
    else:
        form = BoardForm()
    context = {
        'team_id': team_id,
        'form': form,
    }
    data['html_form'] = render_to_string(
        'contents/modal/board_modal.html',
        context=context,
        request=request,
    )
    return JsonResponse(data)


def card_dashboard(request, board_id):
    board = Board.objects.get(pk=board_id)
    cardlists = CardList.objects.filter(board=board)
    context = {
        'board': board,
        'cardlists': cardlists,
        'search_on': True,
    }
    return render(request, 'contents/card_dashboard.html', context=context)


@login_required
def card_list_make(request, board_id):
    data = {}
    if request.method == 'POST':
        form = CardListForm(request.POST)
        if form.is_valid():
            form.save(board_id=board_id)
            data['form_is_valid'] = True
            board = Board.objects.get(pk=board_id)
            cardlists = CardList.objects.filter(board=board)
            context = {
                'board': board,
                'cardlists': cardlists,
                'search_on': True,
            }
            data['html_cardlist_list'] = render_to_string(
                'contents/partial/partial_card_list.html',
                context=context,
                request=request,
            )
    else:
        form = CardListForm()
    context = {
        'form': form,
        'board_id': board_id,
    }
    data['html_form'] = render_to_string(
        'contents/modal/card_list_modal.html',
        context=context,
        request=request,
    )
    return JsonResponse(data)


@login_required
def card_make(request, cardlist_id):
    data = {}
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            board_id = form.save(cardlist_id=cardlist_id)
            data['form_is_valid'] = True
            board = Board.objects.get(pk=board_id)
            cardlists = CardList.objects.filter(board=board)
            context = {
                'board': board,
                'cardlists': cardlists,
                'search_on': True,
            }
            data['html_cardlist_list'] = render_to_string(
                'contents/partial/partial_card_list.html',
                context=context,
                request=request,
            )
    else:
        form = CardForm()
    context = {
        'cardlist_id': cardlist_id,
        'form': form,
    }
    data['html_form'] = render_to_string(
        'contents/modal/card_modal.html',
        context=context,
        request=request,
    )
    return JsonResponse(data)


@login_required
def update_card_position(request, board_id):
    if request.method == 'POST':
        # 카드별 카드리스트 id 값 업데이트
        cards = eval(request.body.decode("utf-8"))
        list_id = cards['list_id']
        positions = cards['positions'].split(';')
        if positions[0] != '':
            card_list = Card.objects.filter(pk__in=positions)
            card_list.update(cardlist=list_id)
        return redirect('dashboard:card_list', board_id=board_id)
    else:
        return redirect('dashboard:card_list', board_id=board_id)
